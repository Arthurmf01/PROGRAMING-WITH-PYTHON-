#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:38:49 2018

@author: arthurmaroquenefroissart
"""

#%%

rock_bands = {
    "beatles": {
        "John" : "Sings",
        "George" : "Guitar", 
        "Paul" : "Bass Guitar", 
        "Ringo": "Play drums"        
    },
    "Ramones" : {
        "Joey":"Sings",
        "Johny" : "Guitar"    
        }
}
    
for band_name in rock_bands : 
    print ("The members of the " + band_name+ "are:")
    
    for member_name in rock_bands[band_name] : 
        print("-" + member_name + ":" + rock_bands[band_name][member_name])
        


#%%

ingredients = {
  "potatoes": 3,
  "celery": 1,
  "onion": 1
}

#%%

#1. Create a function that receives a text and returns the frequency of
#each word in the text (as a dictionary).
#%%
word = input("Enter a word")

Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,26): 
    print(word.count(Alphabet[i]))
    
#%%

frequency_dictionary = {}
for word in "hello world".split() : 
    if word in frequency_dictionary : 
        
        


#%%
2. Create a function that uses the previously generated dictionary and
   prints a bars diagram of the frequencies.  For example, the
   following:

   #+BEGIN_SRC 
   dictionary = {"a": 4, "hello": 1, "world": 3, "another": 2}
   diagram(dictionary)
   #+END_SRC 

   should print:

   #+BEGIN_SRC 
   a       | ****
   hello   | *
   world   | ***
   another | **
   #+END_SRC   
   
3. re-implement the phonebook example using a dictionary instead of
   two lists.



for key in ingredients: 
    print("I have " + str(ingredients[key]) + " " + key )