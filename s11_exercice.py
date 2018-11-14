#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:11:25 2018

@author: arthurmaroquenefroissart
"""

message = "this is a hidden message"


#%% White exercice : create a more accurate version of calculate_volume_cilinder 
#and calculate_volume_sphere that gets the pi constant from the math module

import math 

#%%

def calculate_volume_cilinder (r,h):
    print (pi* r**2 *h)
    
#%%
    
def calculate_volume_sphere (r,h):
    print ((4*pi)/3*r**3)

#%% Blue Belt : Investigate how to create histograms using the matplotlib library. 
# Create a function that uses the matplotlib library to plot the histogram of the grade 
#distribution in an imaginary IE class with 100 students.  Remember that there
# are 15% pass, 35% proficiency, 35% excellence, and 15% honors in a class.


import matplotlib
import numpy as np
import matplotlib.pyplot as plt

class_ranking = (0.15,0.35,0.35,0.15)


ind = np.arange(len(class_ranking))  # the x locations for the groups
width = 0.50  #the width of the bar 

fig, ax = plt.subplots()
histogram_1 = ax.bar([0,1,2,3], class_ranking,
                color='SkyBlue', label='Class Proficiency')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('% of the class')
ax.set_title('Histogram of the grade of Class MCBT/MDBI')
ax.set_xticks(ind)
ax.set_xticklabels(('Pass', 'Proficiency', 'Excellence', 'Honors'))


#%% Black Belt 