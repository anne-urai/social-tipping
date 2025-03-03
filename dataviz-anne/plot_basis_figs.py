'''
Code for visualizing data from social tipping experiment
Anne Urai, Leiden University, 2025

'''

#%% imports
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns 
sns.set_style('darkgrid')
from utils_path import folder_path, figures_folder
from pathlib import Path

#%%
# find out how much data we have - skip hidden files on Jdrive
all_files = [f for f in (Path(folder_path) / 'data').rglob('*.csv') 
             if not f.name.startswith('.')]

#%%
big_df = []
for f in reversed(all_files):
    # load in the raw datafile
    print(f)
    try: df = pd.read_csv(f)
    except: df = pd.read_csv(f, sep=';') # for some reason oTree uses ; as a separator sometimes

    ## clean up to keep only the data that I need
    find_response_columns = ['session_code', 'participant.code', 'participant.id_in_session', #'nick_name',
                             'chose_tao', 'chose_eta', 'timeChoice', 'timeResults']
    response_columns = [c for c in df.columns if any(y in c for y in find_response_columns)]
    df = df[response_columns]

    # wrangle
    df2 = pd.melt(df, id_vars=['participant.code', 'participant.id_in_session'])
    round  = df2["variable"].str.split(".", expand=True)
    df2["round"] = round[1]
    df2["var"] = round[3]
    df2["player"] = df2["participant.code"]
    #df2["player_id"] = df2["participant.id_in_session"]

    #TODO: which players are bots? what about the 3 without RTs or choices?
    #  Good to note is that the players sitting in for confederate bots were always players 3, 5, 9, and 13 in the groups.
    df2['is_bot'] = df2['participant.id_in_session'].isin([3,5,9,13])
    df2 = df2[['player', 'is_bot', 'round', 'var', 'value']]

    # pivot again
    df3 = pd.pivot_table(df2, columns='var', index=['round', 'player', 'is_bot'], values='value').reset_index()
    df3['game'] = f.name.split('.')[0] # save the name of each game, including date
    df3['round'] = df3['round'].astype(int)
    df3['choice'] = (df3.chose_eta - df3.chose_tao).map({-1:0, 0:np.nan, 1:1})
    df3 = df3[['game', 'round', 'player', 'is_bot','choice', 'timeChoice', 'timeResults']]
    big_df.append(df3)

# make one big df
df = pd.concat(big_df).sort_values(by=['game', 'round', 'is_bot','player']).reset_index()

#%% some plotting
# lineplot of average behavior
g = sns.PairGrid(data=df, y_vars=["choice", "timeChoice", "timeResults"], 
                 x_vars=["round"], hue='game', aspect=2)
g.map(sns.lineplot, style=df.is_bot, markers=True)
g.map(sns.lineplot, estimator=None, alpha=0.1, units=df.player)

g.set(xlim=[0,24])
g.savefig(Path(figures_folder) / 'mean_behavior_per_group.png')

# # variance
# g = sns.PairGrid(data=df, y_vars=["choice", "timeChoice", "timeResults"], 
#                  x_vars=["round"], hue='game', aspect=2)
# g.map(sns.lineplot, marker='o', estimator='std')
# g.set(xlim=[0,24])
# g.savefig(Path(figures_folder) / 'var_behavior_per_group.png')

# g = sns.FacetGrid(data=df, y_vars=["choice", "timeChoice", "timeResults"], 
#                  x_vars=["round"], hue='game', aspect=2)
# g.map(sns.lineplot, marker='o')
# g.map(sns.lineplot, estimator=None, alpha=0.1, units=df.player, marker='.')

# g.set(xlim=[0,24])
# g.savefig(Path(figures_folder) / 'mean_behavior_per_group.png')


# # %%

# %%
