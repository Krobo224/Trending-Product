"""
Adding links for every products

"""
from main import *
import pandas as pd
from pytrends.request import TrendReq
import csv
from search_link import*

def addProductLink(productList):
    for product in productList:
       
        df = pd.read_csv(product+".csv")
        for ind in df.index:
                        
            url = df['query'][ind]
            url = search_q(url+' flipkart',url)
            if(url != "~"):
                df.loc[ind, 'Product_Link'] =url
                # lines[3] = url
                df.to_csv(product+".csv", index=False)
            else:
                df.loc[ind, 'Product_Link'] = "Add this product in flipkart"
                # lines[3] = url
                df.to_csv(product+".csv", index=False)
            print("Links added for "+df['query'][ind]+" in "+product+".csv file.............\n")
                        