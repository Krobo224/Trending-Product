"""Fetching the flipkart trending product links from Google API
"""

from pytrends.request import TrendReq
import os
from fetch import*
from add_link import*
from null_remove import *
from merge import *




pytrends = TrendReq(hl='en-US', tz=360)

# list1 = ['Jeans','Shirts','Shorts','T-Shirts','Track Pants','Cargos', 'Raincoats', 'Jwellery', 'Sandals',
#           'Sarees','Kurtas','Kurtis','Gown','Palazzos','Heels','Watches','Baby Toys','Mobiles','Refrigerators','Washing Machine','Air Conditioners'
#           ,'Camera','Bluetooth','Speaker','Bagpack','Beds','Blankets','Mattress','Sofa Beds','Sunglasses','Wardrobe','Water Bottle']

list1=['Shoes']

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    
    fetch(list1)
    addProductLink(list1)
    removeNull(list1)
    mergeAll(list1)
    
       
    
