#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import osmium as osm
import pandas as pd
import numpy as np
from OSM_handler import OSMHandler_N, OSMHandler_W_tags, OSMHandler_W_nodes, OSMHandler_R_tags, OSMHandler_R_mems


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

