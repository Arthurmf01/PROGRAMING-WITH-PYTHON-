#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:15:41 2018

@author: arthurmaroquenefroissart
"""

#2. Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url.

#%%
import requests

def github_api_repository(user):
    url="https://api.github.com/users/{}/repos".format(user)
    
    repositories = requests.get(url).json()

    for repository in repositories:
              
        print("The name of the Github's repository is the following :{} \n The main_language is:{} \n The number_of_stars is:{} \n Here is the url:{} \n".format(
    repository["name"],repository["language"],str(repository["stargazers_count"]),repository["url"]))