#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:46:03 2018

@author: arthurmaroquenefroissart
"""
#%%
# Exercises
#1. 2 points. Imagine you’re creating an application for handling the stock
#of a small shop, and controlling when things go bad in the warehouse.
#Given the following class:
#class Product:
#def _init_(self, name, quality):
#self.name = name
#self.quality = quality
#We have a function that calculates the degrading quality of different
#products in a shop.
#Create all the tests you find meaningful for the following function.
 
class Product():
    
    def __init__(self,name,quality):
        self.name=name
        self.quality=quality

potato1=Product("potato",8)
cheese1=Product("cheese",6)

potato2=Product("potato",15)
cheese2=Product("cheese",20)


potato3=Product("potato",4)
cheese3=Product("cheese",4)


potato4=Product("potato",0)
cheese4=Product("cheese",1)


potato5=Product("potato",2.5)
cheese5=Product("cheese",4.5)

def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
             product.quality -= 3






