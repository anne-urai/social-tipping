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
print(all_files)

#%%
big_df = []
for f in (all_files):
    # load in the raw datafile
    print(f)
    try: df0 = pd.read_csv(f)
    except: df0 = pd.read_csv(f, sep=';') # for some reason oTree uses ; as a separator sometimes

    ## clean up to keep only the data that I need
    '''
    # column 'chosen_name' are all responses from real participants
    # column 'conf_choice' are all responses from playing participants (without bot standins) and the bots
    # chose_tao and chose_eta are the responses of all real participants,
    # of which some are standins for the bots who are really playing (the standins know this)
    '''

    find_response_columns = ['session.code', 'participant.code', 'participant.id_in_session', #'nick_name',
                             'conf_choice', 'chosen_name', 'con_strategy', 'break_name',
                             'chose_tao', 'chose_eta', 'timeChoice', 'timeResults'] 
    response_columns = [c for c in df0.columns if any(y in c for y in find_response_columns)]
    df1 = df0[response_columns]

    # convert the columns that are strings into numbers for pivoting later
    find_response_columns = ['conf_choice', 'chosen_name'] 
    response_columns = [c for c in df0.columns if any(y in c for y in find_response_columns)]    
    for r in response_columns:
        df1[r] = (df1[r]).map({'Tao':-1, 'Eta':1, np.nan:0, 'X':0})

    # wrangle
    df2 = pd.melt(df1, id_vars=['session.code', 'participant.code', 'participant.id_in_session'])
    round  = df2["variable"].str.split(".", expand=True)
    df2["round"] = round[1].astype(int)
    df2["session"] = df2["session.code"]
    df2["var"] = round[3]
    df2["player"] = df2["participant.code"]
    df2["player_id"] = df2["participant.id_in_session"].astype(int)
    #  Good to note is that the players sitting in for confederate bots were always players 3, 5, 9, and 13 in the groups.
    df2['is_bot'] = df2['player_id'].isin([3,5,9,13])

    # pivot again
    df3 = pd.pivot_table(df2, columns='var', index=['session', 'round', 
                                                    'player_id', 'player', 'is_bot'], 
                         values='value', fill_value=np.nan).reset_index()
    df3['game'] = f.name.split('.')[0] # save the name of each game, including date

    # this one is for after the bots have had their vote
    df3['displayed_choice_eta'] = (df3.chose_eta - df3.chose_tao).map({-1:0, 0:np.nan, 1:1})
    df3['player_choice_eta'] = (df3.chosen_name + df3.conf_choice).map({-1:0, 0:np.nan, 1:1})

    # append together
    big_df.append(df3[['game', 'session', 'round', 'player', 'player_id', 'is_bot',
               'displayed_choice_eta', 'player_choice_eta', 'timeChoice', 'timeResults']]
)

# make one big df
df = pd.concat(big_df).sort_values(by=['game', 
                                       'session', 'round', 
                                       'player_id', 'player', 'is_bot']).reset_index()
df.to_csv('/data/clean_df.csv')

#%% some plotting
# lineplot of average behavior
g = sns.PairGrid(data=df, y_vars=["choice", "timeChoice", "timeResults"], 
                 x_vars=["round"],  hue='game', aspect=2)
g.map(sns.lineplot, style=df.is_bot, 
      markers=True)
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

# %% heatmaps

fig, axs = plt.subplots(df.session.nunique(), 2, 
                        sharex=True, sharey=True)

for vix, v in enumerate(['player_choice_eta', 'displayed_choice_eta']):
    for dix, (sess, d) in enumerate(df.groupby('session')):
        sns.heatmap(data=d.pivot(index='player_id', 
                                    columns='round', 
                                    values=v), ax=axs[dix, vix],
                                    linewidths=.5, cbar=False)
        axs[dix, vix].set(title=sess, xticks=range(df['round'].max()), yticks=range(df['player_id'].max()),
                          xlabel='')

# %%
