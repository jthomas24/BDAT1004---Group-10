#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
        return texts
    except:
        return []

def real_time_price(stock_code):
    url = f"https://finance.yahoo.com/quote/{stock_code}"
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'html.parser')
        class_path = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"
        texts = web_content_div(web_content, class_path)
        return texts
    except ConnectionError as e:
        print("Connection Error:", e)
        return []

# Example usage:
stock_code = "TSLA"
price = real_time_price(stock_code)
print("Real-time price of", stock_code, "is:", price)


# In[ ]:




