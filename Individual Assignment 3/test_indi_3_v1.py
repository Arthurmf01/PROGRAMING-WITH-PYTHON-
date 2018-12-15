#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:16:47 2018

@author: arthurmaroquenefroissart
"""

#def recalculate_quality(product):
    #if product.name == "potato":
        #product.quality = product.quality - 0.5
    #elif product.name == "cheese":
        #product.quality = product.quality - 2
    #else:
        #if product.quality < 5:
             #product.quality -= 3
#%%

from Exercices_V1 import recalculate_quality

from Exercices_V1 import Product

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


def test_recalculate_quality_first():
    recalculate_quality(potato1)
    assert potato1.quality==7.5
    recalculate_quality(cheese1)
    assert cheese1.quality==4
     
    
def test_recalculate_second():
    recalculate_quality(potato2)
    assert potato2.quality==14.5
    recalculate_quality(cheese2)
    assert cheese2.quality==18

    
def test_recalculate_third():
    recalculate_quality(potato3)
    assert potato3.quality==3.5
    recalculate_quality(cheese3)

    
    
def test_recalculate_fourth():
    recalculate_quality(potato4)
    assert potato4.quality==-0.5
    recalculate_quality(cheese4)

    
    
def test_recalculate_fifth():
    recalculate_quality(potato5)
    assert potato5.quality==2
    recalculate_quality(cheese5)
