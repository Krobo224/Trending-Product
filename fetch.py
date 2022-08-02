""" This file will fetch all trending products from google api
"""

from main import *
import pandas as pd
import  pytrends
from pytrends.request import TrendReq
import csv

def fetch(list1):
    for var in list1:
        try:
            pytrends.build_payload(kw_list=[var])
            related_queries = pytrends.related_queries()
            df2 = pd.DataFrame(related_queries[var]['rising'])
            df2.to_csv(var+'.csv')
            print("Created "+var+".csv file................\n")
        except:
            print("Failed to create "+var+".csv file................\n")
            continue;
