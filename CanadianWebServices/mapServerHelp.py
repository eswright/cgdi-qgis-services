# -*- coding: utf-8 -*-
"""
/***************************************************************************
Helper functions to retrieve information about mapservers
"""
import urllib.request, json

# returns a list containing all layer IDs of a mapserver with url
def getIDs(url):
    response = urllib.request.urlopen(url)
    json_file = json.loads(response.read())
    
    layers = (json_file['layers'])
    
    id_list = list()
    
    for layer in layers:
        id_list.append(layer['id'])
        
    return id_list

# returns a list containing all layer names of a mapserver with url    
def getNames(url):
    response = urllib.request.urlopen(url)
    json_file = json.loads(response.read())
    
    layers = (json_file['layers'])
    
    name_list = list()
    
    for layer in layers:
        name_list.append(layer['name'])
        
    return name_list
