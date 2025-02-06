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
all_files = [f for f in Path(folder_path).rglob('*.csv') if not f.name.startswith('.')]

#%%
for f in reversed(all_files):
    # load in the raw datafile
    print(f)
    try:
        df = pd.read_csv(f) # for some reason oTree uses ; as a separator
    except:
        df = pd.read_csv(f, sep=';') # for some reason oTree uses ; as a separator

    ## clean up to keep only the data that I need
    find_response_columns = ['session_code', 'participant.code', #'nick_name',
                             'chose_tao', 'chose_eta', 'timeChoice', 'timeResults']
    response_columns = [c for c in df.columns if any(y in c for y in find_response_columns)]
    df = df[response_columns]

    # wrangle
    df2 = pd.melt(df, id_vars=['participant.code'])
    round  = df2["variable"].str.split(".", expand=True)
    df2["round"] = round[1]
    df2["var"] = round[3]
    df2["player"] = df2["participant.code"]
    df2 = df2[['player', 'round', 'var', 'value']]

    # pivot again
    df3 = pd.pivot_table(df2, columns='var', index=['player', 'round'], values='value').reset_index()
    df3['game'] = g

    ## we plot some things

    sns.heatmap(df3, x='round', y='player')
# %%
