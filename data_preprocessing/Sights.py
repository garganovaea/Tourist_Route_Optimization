#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

class sights(df_tags, df_wnodes, df_nodes):
    
    '''
    Search for a list of nodes ids which are sights and can be reached by people.
    '''
    
    def __init__(self): 
        self.sights = []
        self.df_tags = df_wtags
        self.df_wnodes = df_wnodes
        self.df_nodes = df_nodes
        
    def flatten(self, compl_list): 
        '''
        Return the flattened list from complicated list
        '''
        return [item for sublist in compl_list for item in sublist]
    
    def allowed_nodes(self):
        '''
        Find nodes where people can walk
        Return: the ids list
        '''
        key_list = self.df_tags.tagkey.values
        value_list = self.df_tags.tagvalue.values
        allows = []

        for i in range(len(key_list)):
            if key_list[i] != None:
                if (key_list[i] == 'foot') & (value_list[i] == 'yes'):
                    allows.append(self.df_tags.loc[i].id)
                elif (key_list[i] == 'highway'):
                    if (value_list[i] == 'footway') | (value_list[i] == 'service') | (value_list[i] == 'pedestrian'):
                        allows.append(self.df_tags.loc[i].id)

        allows = list(set(allows))
        allows_f = self.flatten([self.df_wnodes[self.df_wnodes['id'] == allows[i]
                              ].node.values.tolist() for i in range(len(allows))])
        
        return allows_f
        
    def find_ids(self):
        '''
        Return the sights id list
        '''
        ids = []

        for value in value_sight:
            need_df = self.df_tags[self.df_tags['tagvalue'] == value]
            if len(need_df) != 0:
                ids.append(need_df.id.values)
        
        ids = self.flatten(ids)

        return ids
    
    def find_sights(self, ids):
        '''
        Return the sights nodes list
        '''
        sights = []
        for ID in ids:
            d = self.df_wnodes[self.df_wnodes['id'] == ID].node.values
            sights.append(d[np.random.randint(len(d))])

        sights_from_nodes = flatten(self.find_ids(self.df_nodes))
        sights = sights + sights_from_nodes
        sights = list(set(sights))
        
        self.sights = sights
        
        return sights

    def nearest_route(self, sight, allows_f):
        '''
        Change the id of the not available nodes on the nearest available
        '''
        new_df = self.df_nodes.loc[self.df_nodes['id'].isin(allows_f)]

        all_lats = new_df.lat.values.tolist()
        all_lons = new_df.lon.values.tolist()

        sight_lat = df_nodes[df_nodes['id'] == sight].lat.values[0]
        sight_lon = df_nodes[df_nodes['id'] == sight].lon.values[0]

        dif_lats = list(np.absolute(all_lats - sight_lat))
        dif_lons = list(np.absolute(all_lons - sight_lon))

        sum_dif = [x + y for x, y in zip(dif_lats, dif_lons)]

        return df_nodes[(df_nodes['lat'] == all_lats[sum_dif.index(min(sum_dif))])].id.values[0]
    
    def change(self, allows_f):
        '''
        Make all sights in the list available 
        '''
        new_sights = []
        for sight in self.sights:
            if sight in allows_f:
                new_sights.append(sight)
            else:
                new_sights.append(self.nearest_route(sight, allows_f))

        self.sights = new_sights
        
        return new_sights

    def save(self):
        '''
        Save the sights as .txt file
        '''
        with open("Sights.txt", "w") as file:
            print(*self.sights, file=file)

