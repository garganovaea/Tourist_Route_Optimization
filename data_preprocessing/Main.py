#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import osmium as osm
import pandas as pd
import numpy as np
from geopy import distance

from OSM_handler import OSMHandler_N, OSMHandler_W_tags, OSMHandler_W_nodes, OSMHandler_R_tags, OSMHandler_R_mems
from Sights import Sights_class
from Adjacency_matrix import Adj_matrix_class


def osm_to_df(file, data_colnames, osmhandler, name):
    '''
    Return DataFrame with data from OSM.XML file and create the CSV file with it
    Args:
        file: Geodata file from OpenStreetMap
        data_colnames: the list of names for columns in DataFrame
        osmhandler: appropriate class from OSM_handler.py
        name: the name of the CSV file with returned DataFrame
    '''

    # scan the input file and fills the handler list accordingly
    osmhandler.apply_file(file, locations=True)

    df = pd.DataFrame(osmhandler.osm_data, columns=data_colnames)
    df.to_csv(name)

    return df


# Data
df_Nodes = osm_to_df('map.osm', [
                     'id', 'lon', 'lat', 'num_tags', 'tagkey', 'tagvalue'], OSMHandler_N(), 'Nodes.csv')

df_Ways_t = osm_to_df('map.osm', ['id', 'num_tags', 'tagkey', 'tagvalue'],
                      OSMHandler_W_tags(), 'Ways_tags.csv')

df_Ways_n = osm_to_df('map.osm', ['id', 'num_nodes', 'node'],
                      OSMHandler_W_nodes(), 'Ways_nodes.csv')

df_Rels_t = osm_to_df('map.osm', ['id', 'num_tags', 'tagkey', 'tagvalue'],
                      OSMHandler_R_tags(), 'Relations_tags.csv')

df_Rels_m = osm_to_df('map.osm', ['id', 'num_mems', 'type', 'ref', 'role'],
                      OSMHandler_R_mems(), 'Relations_members.csv')


# DataFrame with keys of sights
value_sight = ['artwork', 'attraction', 'gallery', 'museum', 'viewpoint', 'cathedral', 'chapel', 'church',
               'mosque', 'shrine', 'synagogue', 'temple', 'fountain', 'theatre', 'aircraft', 'battlefield',
               'cannon', 'castle', 'city_gate', 'highwater_mark', 'locomotive', 'manor', 'memorial',
               'monastery', 'monument', 'railway_car', 'ruins', 'ship', 'tank']

tags_sights = pd.DataFrame()
tags_sights['value'] = value_sight

# Find sights
result = Sights_class(df_Ways_t, df_Ways_n, df_Nodes)

ids = result.find_ids() # ids of sights
allows = result.allowed_nodes()

result.find_sights(ids) # nodes of sights
result.change(allows)
result.save()


# Adjacency matrix
matrix = Adj_matrix_class().create_matrix()
adjacency_matrix = matrix.weighted_matrix()

adjacency_matrix.to_csv('Adj_Matrix.csv')

