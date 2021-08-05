#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from geopy import distance


class Adj_matrix_class(df_Ways_n, df_Nodes):
    
    def __init__(self): 
        self.matrix = pd.DataFrame(0, index=nodes, columns=nodes)
        self.df_Ways_n = df_Ways_n
        self.df_Nodes = df_Nodes
        self.nodes = df_Nodes.id.unique()
        
    def create_matrix(self):
        '''
        Create adj matrix
        '''
        for i in self.nodes:
            # Adjacency list for every way
            adjs = list(self.df_Ways_n[self.df_Ways_n['id'] == i].node)
            # Mark 1 in matrix
            for j in range(len(adjs)-1):
                self.matrix.at[adjs[j], adjs[j+1]] = 1
                self.matrix.at[adjs[j+1], adjs[j]] = 1  # For a symmetric matrix
            
        return self.matrix
            
    def weighted_matrix(self):
        '''
        Create weighted adj matrix calculating distances based on geographical coordinates
        '''
        w_matrix = pd.DataFrame(0, index=nodes, columns=nodes)
        for i in self.nodes:
            for j in self.nodes:
                if self.matrix.at[i, j] == 1:
                    node_1 = np.array([self.df_Nodes[self.df_Nodes['id'] == i].lat.values[0],
                                       self.df_Nodes[self.df_Nodes['id'] == i].lon.values[0]])
                    node_2 = np.array([self.df_Nodes[self.df_Nodes['id'] == j].lat.values[0],
                                       self.df_Nodes[self.df_Nodes['id'] == j].lon.values[0]])
                    dist = distance.distance(node_1, node_2).m  # In meters
                    w_matrix.at[i, j] = dist
                    w_matrix.at[j, i] = dist
        return w_matrix

