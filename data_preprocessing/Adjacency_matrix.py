#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from geopy import distance


df_Nodes = pd.read_csv('Nodes.csv')
df_Nodes = df_Nodes.drop('Unnamed: 0', 1)

df_Ways_n = pd.read_csv('Ways_nodes.csv')
df_Ways_n = df_Ways_n.drop('Unnamed: 0', 1)


matrix = pd.DataFrame(0, index=nodes, columns=nodes)

for i in allows:
    # Adjacency list for every way
    adjs = list(df_Ways_n[df_Ways_n['id'] == i].node)
    # Mark 1 in matrix
    for j in range(len(adjs)-1):
        matrix.at[adjs[j], adjs[j+1]] = 1
        matrix.at[adjs[j+1], adjs[j]] = 1  # For a symmetric matrix


# Calculating distances based on coordinates

nodes = df_Nodes.id.unique()

for i in nodes:
    for j in nodes:
        if matrix.at[i, j] == 1:
            node_1 = np.array([df_Nodes[df_Nodes['id'] == i].lat.values[0],
                               df_Nodes[df_Nodes['id'] == i].lon.values[0]])
            node_2 = np.array([df_Nodes[df_Nodes['id'] == j].lat.values[0],
                               df_Nodes[df_Nodes['id'] == j].lon.values[0]])
            dist = distance.distance(node_1, node_2).m  # In meters
            matrix.at[i, j] = dist
            matrix.at[j, i] = dist

matrix.to_csv('Adj_Matrix.csv')

