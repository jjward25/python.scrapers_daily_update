import os
import glob
import pandas as pd
#os.chdir(r"C:\Users\Josep\OneDrive\Desktop\Coding\python.ca-scrapers")

#extension = 'csv'
#all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# Modules
from run_gov import *
from run_headlines import *
from run_opeds import *
from stembiz import *

combined_df = pd.DataFrame()
combined_df = combined_df.append(gov_df)


#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined.csv", index=False, encoding='utf-8-sig')