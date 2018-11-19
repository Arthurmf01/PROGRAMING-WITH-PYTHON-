#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:26:01 2018

@author: arthurmaroquenefroissart
"""
#%%

from white_blue_belt import Extra

def test_extra_2_time_yes():
    assert Extra("yes","yes") == 15
    
def test_extra_yes_and_no():
    assert Extra("yes","no") == 10
    assert Extra ("no","yes") == 5 

def test_extra_2_times_no():
    assert Extra ("no","no") == 0
#%%