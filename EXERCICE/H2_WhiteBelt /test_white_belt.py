#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 12:53:25 2018

@author: arthurmaroquenefroissart
"""

#%%

from white_blue_belt import checkout_eshop


Guitar = {"item1":1000}
PickBox = {"item2":5}
GuitarStrings = {"item3":10}
email_price_priority = 10
info_insurance_price = 5
extra_eshop = 0

def test_checkout_eshop_return ():
    assert checkout_eshop([Guitar]) == 1000
    assert checkout_eshop([PickBox]) == 5
    assert checkout_eshop([GuitarStrings]) == 10
    assert checkout_eshop([]) == "Please select at least one element in our E-shop website before check out"
    assert checkout_eshop([Guitar, PickBox, GuitarStrings]) == 1015
    assert checkout_eshop([PickBox,PickBox]) == 10
    
def test_checkout_eshop_emptycart():
    emptycart=[]
    assert checkout_eshop(emptycart)=="Please select at least one element in our E-shop website before check out"
#%%
