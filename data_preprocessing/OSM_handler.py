#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import osmium as osm
import pandas as pd
import numpy as np
from geopy import distance

# Nodes

class OSMHandler_N(osm.SimpleHandler):
    
    """ Сollecting the necessary data from OSM.XML file. """
    
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        if len(elem.tags) == 0:
            self.osm_data.append([elem.id,
                                  elem.location.lon,
                                  elem.location.lat,
                                  len(elem.tags)])
        else:
            for tag in elem.tags:
                self.osm_data.append([elem.id,
                                      elem.location.lon,
                                      elem.location.lat,
                                      len(elem.tags),
                                      tag.k,
                                      tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")


# Ways (tags)

class OSMHandler_W_tags(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        if len(elem.tags) == 0:
            self.osm_data.append([elem.id,
                                  len(elem.tags)])
        else:
            for tag in elem.tags:
                self.osm_data.append([elem.id,
                                      len(elem.tags),
                                      tag.k,
                                      tag.v])

    def way(self, w):
        self.tag_inventory(w, "way")


# Ways (nodes)

class OSMHandler_W_nodes(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def node_inventory(self, elem, elem_type):
        if len(elem.nodes) == 0:
            self.osm_data.append([elem.id,
                                  len(elem.nodes)])
        else:
            for node in elem.nodes:
                self.osm_data.append([elem.id,
                                      len(elem.nodes),
                                      node.ref])

    def way(self, w):
        self.node_inventory(w, "way")


# Relations (tags)

class OSMHandler_R_tags(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        if len(elem.tags) == 0:
            self.osm_data.append([elem.id,
                                  len(elem.tags)])
        else:
            for tag in elem.tags:
                self.osm_data.append([elem.id,
                                      len(elem.tags),
                                      tag.k,
                                      tag.v])

    def relation(self, r):
        self.tag_inventory(r, "relation")


# Relations (members)

class OSMHandler_R_mems(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def mem_inventory(self, elem, elem_type):
        if len(elem.members) == 0:
            self.osm_data.append([elem.id,
                                  len(elem.members)])
        else:
            for member in elem.members:
                self.osm_data.append([elem.id,
                                      len(elem.members),
                                      member.type,
                                      member.ref,
                                      member.role])

    def relation(self, r):
        self.mem_inventory(r, "relation")

