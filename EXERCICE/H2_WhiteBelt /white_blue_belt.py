#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:41:28 2018

@author: arthurmaroquenefroissart
"""
#%% White belt : 
 
#Our e-shop sells the following products:
 #1. Guitar: $1000
  # 2. Pick box: $5
   #3. Guitar Strings: $10
   #Create a function named checkout that takes a list that represents a 
   #shopping cart and returns the total cost of it.  This function should check that 
   #the shopping cart must not be empty.
   #Create also some tests for the function.  Try to think of the corner cases.
   #Hint: you can represent a product as a dictionary with a name and a price.
   
#Blue Belt : 

#You want to give more features to the user, so you decide that you will 
#allow them to purchase an insurance package on their purchase and also priority mail.  
#Consider that these two new services can only be purchase once per order.
 #  1. Insurance: $5
  # 2. Priority mail: $10
 #  Modify your checkout function so it handles these cases correctly, and add
# more tests that check your functionality.
   

#infos: 
#White Belt 
Guitar = {"item1":1000}
PickBox = {"item2":5}
GuitarStrings = {"item3":10}
#Blue Belt 
email_price_priority = 10
info_insurance_price = 5
extra_eshop = 0


# Here is the customer's infos: 
#Here we have in the shopping cart 2 Guitar Strings, 1 Guitar and 1 Pickbox 
shop_cart =[Guitar,Guitar,PickBox,PickBox]




def checkout_eshop(shop_cart):
    if shop_cart == [] :            #return 0 if the shop_cart is EMPTY
       return "Please select at least one element in our E-shop website before check out"
    else:
        
        counter_cart = 0 #counter 
        for item in range(len(shop_cart)):     #Use range to review ALL the function 
            counter_cart = counter_cart + sum(shop_cart[item].values())
    return counter_cart

#%%
    
insurance = "no"
email= "no"

def Extra(email,insurance):
   
    
    if email == "yes"  and insurance == "yes":
        extra_eshop = email_price_priority + info_insurance_price
        return extra_eshop
    elif insurance == "yes" and email == "no":
        extra_eshop = info_insurance_price
        return extra_eshop
    elif insurance == "no" and email == "yes":
        extra_eshop = email_price_priority
        return extra_eshop
    else: 
        extra_eshop = 0
        return extra_eshop 
    
    