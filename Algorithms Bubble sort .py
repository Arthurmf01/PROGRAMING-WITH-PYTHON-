#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:19:00 2018

@author: arthurmaroquenefroissart
"""

#%%

list = []
def bublesort (list): 
    maxnumber= list[0]
    temp = list[1]
    for i in range(0,len(list),1):
        if maxnumber > list[temp]:
            temp     = list[0]
            list [0] = list [1]
            list [1] = temp
            
#%%Solution

input_list = [2,44,6,7,890,77,1,7,9,899,8,87,876,654,446,6]

#%%

def bubble (lst): 
    
    y = 0
    
    while y < len(lst):
        
        x = 0 
        while x < len(lst) - 1 : 
            if lst[x] > lst[x +1]:
                temp = lst[x]
                lst[x] = lst[x+1]
                lst[x+1] = temp
            
            x += 1 
        
        y += 1
    print (input_list)
        
#%%  
    
def bubble_for(lst):
    for y in range(len(lst)-1):
        
        print(list(range(len(lst) - y - 1)))
        for x in range(len(lst) -y -1):
            if lst[x]>lst[x+1]:
                temp = lst[x]
                lst[x] = lst[x+1]
                lst[x+1] = temp
                
                
#%%
                

    
    
            
#%%
    
    1.compare 
    
    2.Swap
    