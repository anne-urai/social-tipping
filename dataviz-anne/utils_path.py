import os
#ToDo: rewrite with Path

# Specify the path to the folder containing your CSV files
#ToDo: store this info in a better file
usr = os.path.expanduser("~")
if usr == '/Users/uraiae': # mounted using mountainduck on macbook pro
    folder_path = '/Volumes/macOS/Users/uraiae/SOCIAL-TIPPING.localized/'
else: # for local data
    folder_path = "./data/subjects"

# figures stay in the repo for now
figures_folder = os.path.join(os.getcwd(), 'figures') # to save