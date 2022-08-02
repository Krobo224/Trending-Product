"""
Will search for product link available on Flipkart through beautifilsoup python package.
"""

from googlesearch import search
from nltk.tokenize import WhitespaceTokenizer

# Create a reference variable for Class WhitespaceTokenizer
tk = WhitespaceTokenizer()


def search_q(question,product):
       geek = tk.tokenize(product)
    # print(geek[0])
       try:
        for j in search(question, tld="co.in", num=1, stop=1, pause=1):
            if 'flipkart' in j and geek[0] in j:
                return (j)
       except:
          return ("~")