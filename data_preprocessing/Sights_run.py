#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from Sights import sights


df_Nodes = pd.read_csv('Nodes.csv')
df_Nodes = df_Nodes.drop('Unnamed: 0', 1)

df_Ways_n = pd.read_csv('Ways_nodes.csv')
df_Ways_n = df_Ways_n.drop('Unnamed: 0', 1)

df_Ways_t = pd.read_csv('Ways_tags.csv')
df_Ways_t = df_Ways_t.drop('Unnamed: 0', 1)


# DataFrame with keys of sights
value_sight = ['artwork', 'attraction', 'gallery', 'museum', 'viewpoint', 'cathedral', 'chapel', 'church',
               'mosque', 'shrine', 'synagogue', 'temple', 'fountain', 'theatre', 'aircraft', 'battlefield',
               'cannon', 'castle', 'city_gate', 'highwater_mark', 'locomotive', 'manor', 'memorial',
               'monastery', 'monument', 'railway_car', 'ruins', 'ship', 'tank']

tags_sights = pd.DataFrame()
tags_sights['value'] = value_sight


# Find sights
result_sights = sights(df_Ways_t, df_Ways_n, df_Nodes)

ids = result_sights.find_ids()
allows = result_sights.allowed_nodes()

result_sights.find_sights(ids)
result_sights.change(allows)
result_sights.save()

