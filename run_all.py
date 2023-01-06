import os
import glob
import pandas as pd
#os.chdir(r"C:\Users\Josep\OneDrive\Desktop\Coding\python.ca-scrapers")

#extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Modules
from run_gov import *
from run_opeds import *
#from run_stembiz import *

combined_list = [gov_df,opeds_df]
#hud_df

combined_df = pd.concat(combined_list)
#print(combined_df)
print(combined_df)
combined_df.to_csv(r'combined.csv',index=False)
combined_df.to_clipboard()

