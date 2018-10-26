#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:37:35 2018

@author: arthurmaroquenefroissart
"""

#%%

def sum_list(lst): 
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])
    
    
#%%
        
def multiply (lst): 
    if lst == []:
        return 1 
    else lst [1] * multiply (lst[1:])

#%%
    
    
 #Version correction probleme
    
    
    
def merge (a,b):
    new_list = []

    while len(a) > 0 and len(b) > 0 : 
        if a [0] < b [0]:
            new_list.append(a[0])
            a.pop (0)
        else : 
            new_list.append(b[0])
            b.pop(0)
    
    if len(a) == 0: 
        new_list += b
        
    else :
        new_list += a
    
    return new_list
    
#%%

def merge_sort (lst) :
    if len(lst) <= 1:             
        return lst 
    
    middle = len(lst) // 2 
    left = lst [:middle]
    right = lst [middle:]
    
    return (merge(merge_sort(left),merge_sort(right)))


#%%

         #Ma version 


lst = [56,22,86,95, 63,661, 89,765, 47, 761, 23, 34, 64,55,230]

def merge_sort (lst) :
    if len(lst) > 1 : 
        mid = len(lst)//2
        left = lst [:mid]                   #[start:stop:step]
        right = lst [mid:]
        
        merge_sort(left)
        merge_sort(right)
    

        i = 0                                                    #1. 3 variables - one for left, one for right - one to swap value                           
        j = 0
        k = 0
        while i < len(left) and j < len(right):                  #1. Lst took value i if i < len(left)
            if left [i] < right [j]:
                lst[k]= left [i]
                i = i + 1
            else :                                               #2. Lst took value k if j < len(right)
                lst [k] = right [j]
                j = j+1 
            k = k + 1                                            #IMPORTANT: need ot be in the while loop otherwise only for right
        while i < len(left) :                                    #3. Swap Value for left 
            lst[k] = left [i]
            i = i + 1 
            k = k + 1 
        while i > len(right) :                                  #4. Swap Value for right
            lst[k] = right[j]
            j = j+1
            k = k+1
    print("Merging" , lst)
    
#%%

        