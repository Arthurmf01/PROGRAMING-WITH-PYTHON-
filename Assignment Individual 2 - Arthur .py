#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:16:46 2018

@author: arthurmaroquenefroissart
"""

#%%

#Bubble sort Algorithm 

def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
    return lst 
                

#%% 1. maximum value between two indices
#(a) Create a function max_between that takes an unsorted list and 
#two indices and returns what’s the maximum value between those two indices.

lst = [0,4,6,3,5,6,2,-89]
#or    
nums = [0, 12,123,45,76,76,98,176,65,87,90,654]

def max_between_2(lst, start_lst, end_lst):           
   
   if  start_lst < end_lst and start_lst > 0 : 
       end_lst = end_lst + 1                           
       lst_filtered = lst[start_lst:end_lst]
       sorted_lst_filtered = bubble(lst_filtered)
       return sorted_lst_filtered[-1]
   else : 
        return "Please be sure that start index is smaller that end index"
 
#%%
#F#(b) (extra credit) Can you think of a faster implementation of your algorithm
# if you’re ensured that the list is sorted?

 
nums_sorted = [0, 12, 45, 65, 76, 76, 87, 90, 98, 123, 176, 654]
 
def max_between_2_better(lst, start_lst, end_lst):
    
    if start_lst > 0 and start_lst < end_lst: 
        end_lst = end_lst + 1  
        lst_filtered = lst[start_lst:end_lst]
        return lst_filtered[-1]
    else: 
        return "Please be sure that start index is smaller that end index"
#We can clearly verify that it is faster with the folowing function, because the list is already sorted.  :  
#Compute time to verify :   
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))



#%% value appears in both lists
#(a) Create a function appears_in_both that receives two unsorted lists and one integer.
# The function should return True if the integer
# appears in both lists and False otherwise.

lst_1 = [45,3,4,5,6,9,-89,534]
lst_2 = [45,22,9,45,9,76,534,76]
                                                 
def appears_in_both (lst_1,lst_2,k):
    if k in lst_1 and k in lst_2 : 
        return True
    else :       
        return False 
            
#%% (b) (extra credit) Create another version of the function in which the lists are sorted.
    
#Already the faster implementatio above. 
#%%
#3. intersection
#(a) Create a function intersection that receives two lists as param- etes and 
#returns the intersection of them (intersection meaning 
#the elements they have in common).
        
def intersection(lst_1, lst_2): 
    lst_3 = [value for value in lst_1 if value in lst_2] 
    return lst_3 

#%%#(b) (extra credit) could you find a faster implementation if you’re sure 
#that the two lists you receive are sorted?
    
#Already the faster implementation with a "for" loops nested within the list.
    
#Compute time to verify :   
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

    
#%%
#4. difference
#(a) Create a function difference that receives two lists as parametes
# and returns the difference of them
# (difference meaning all the elements they don’t have in common).
            
def difference (lst_1,lst_2):
    lst_3 = [value for value in lst_1 if value not in lst_2] 
    return lst_3 

#%%
#(b) (extra credit) could you find a faster implementation if you’re sure that the two lists you receive are sorted?

#Already the faster implementation