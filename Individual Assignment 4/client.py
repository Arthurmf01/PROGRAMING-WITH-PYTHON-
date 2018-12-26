#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:29:52 2018

@author: arthurmaroquenefroissart
"""

#%%
Exercises
In this exercise we will create an HTTP server to which we can upload a
 graph and in which we can get the degrees of separation between two nodes in the graph.
1. Create a route in the server to which the user can upload a graph using 
JSON and using the POST http method. The JSON data should be passed as part of the request body,
 not in the URL.
2. Create a route to get the degrees of separation between two nodes in the previously uploaded graph.
localhost:5000/degrees_of_separation/<origin>/<destination>.
You can use any code we want from the exercises we’ve done in class
related to graphs.

#%%

graph_example = {
    "a": ["b", "c", "d"],
    "b": ["a","d"],
    "c": ["d"],
    "d": ["c","e"],
    "e": [],
    "f": [],
    "z": ["a","b"],
}

import requests

url = 'http://127.0.0.1:5000/{}'

def upload_graph_test(graph_example):  
    
    data = graph_example
    resquest = requests.post(url.format('upload-graph'), json=data)   
    
    return resquest.json()

upload_graph(graph_example)

def degrees_of_separation(begin, end, graph_example): 
    url = "http://127.0.0.1:5000/degrees-of-separation/" + begin + "/" + end 
    data = graph_example
    resquest = requests.post(url, json=data)
    
    return resquest.json()

degrees_of_separation("c","d",graph_example)

#%%
