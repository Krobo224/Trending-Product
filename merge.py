"""This combines all the CSV files made
"""


from operator import index
import pandas as pd
import glob
import os
from main import*


def mergeAll(list1):
    fileExtension = '.csv'
    fileNames = [i for i in glob.glob(f"*{fileExtension}")]
    
    combined_data = pd.concat([pd.read_csv(f) for f in fileNames])
    combined_data.sort_values(combined_data.columns[2], axis=0, inplace=True, ascending=False)
    
    combined_data =combined_data.iloc[:, 1:]
    combined_data.to_csv('AllTrending.csv', index=False)
    remove_rest(list1)
    
# The below function can be Deleted if we need a trending product within a subcategory (e.g in shoes)
def remove_rest(list1):
    for file in list1:
        file_name = file+'.csv'
        if(os.path.exists(file_name) and os.path.isfile(file_name)):
            os.remove(file_name)
