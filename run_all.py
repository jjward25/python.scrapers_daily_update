import os
import pandas as pd
import glob

from run_gov import *
from run_opeds import *
from run_headlines import *
from run_stembiz import *

path = './'
all_files = glob.glob(os.path.join(path, "*.csv"))
writer = pd.ExcelWriter('daily_update.xlsx', engine='xlsxwriter')

for f in all_files:
    df = pd.read_csv(f)
    df.to_excel(writer, sheet_name=os.path.splitext(os.path.basename(f))[0], index=False)

writer.close()

os.system("start EXCEL.EXE daily_update.xlsx")