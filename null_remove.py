"""Will remove the products those doesn't have links in them
"""
import os
import pandas as pd

def removeNull(productList):
    for product in productList:
        df = pd.read_csv(product+'.csv')
        print("There are ", df['Product_Link'].isnull().sum(), "product(s) in", product,"which have no links present")
        df = df.dropna(subset=['Product_Link'])
        df.to_csv(product+'.csv', index=False)
