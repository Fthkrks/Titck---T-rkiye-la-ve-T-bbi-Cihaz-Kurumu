#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import sqlite3





df = pd.read_excel("ilaç listesi.xlsx")
db = sqlite3.connect('sqlite.db')
dfs = pd.read_excel('ilaç listesi.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db)
    print(f'{df} başarıyla eklendi')


# In[ ]:




