#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:21:31 2018

@author: arthurmaroquenefroissart
"""
#%%

import requests

def add_contact(name,phone):
    
    url = "http://127.0.0.1:5000/add_contact/" + name + "/" + phone
    
    response = requests.get(url).json()
    
    return response

add_contact("mum","0687678977")

#%%
def get_contact(name):
    
    url = "http://127.0.0.1:5000/get_contact/" + name 
    
    response = requests.get(url).json()
    
    return response

get_contact("Dad")

#%%
def delete_contact(name):
    
    url = "http://127.0.0.1:5000/delete_contact/" + name 
    
    response = requests.get(url).json()
    
    return response

delete_contact("Dad")

#%%

def update_contact(name,phone):
    
    url = "http://127.0.0.1:5000/update_contact/" + name + "/" + phone
    
    response = requests.get(url).json()
    
    return response

update_contact("mum","0687678977")
