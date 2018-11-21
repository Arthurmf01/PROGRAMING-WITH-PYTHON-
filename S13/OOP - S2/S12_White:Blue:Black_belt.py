#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:38:46 2018

@author: arthurmaroquenefroissart
"""
#%% White 
#Create a Student class that has the following attributes:
#name
#last name
#age
#master (either MCSBT or MDBI)
#Make sure you parametrize all those fields in the constructor.
#blue 
#add a print_student method in the Student class that prints a line like
# follows for the object
#Pepe García is a 55 year old student of the MCSDBI masters programme
#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call print_student on each one to print its description.


class student : 
    
    all_names = []
    
    def __init__ (self,name,last_name, age, master):
        
        self.name = name 
        self.last_name = last_name
        self.age = age
        self.master = master 
        student.all_names.append(self)
        print("{} {} is a {} year old student of the {} masters programme\n ".format(self.name,self.last_name, self.age,self.master))


Alejandro = student("Alejandro", "Meneses", "27", "MCSBT")
Agata = student("Agata", "Kaczmarek", "31","MDBI")
Anastasia = student("Anastasia", "Lasunina", "25", "MDBI")
Anikken = student("Anikken", "Barstad-Gjeruldsen", "27", "MDBI")
Candela = student("Candela", "Noya", "24", "MDBI")
Daniil = student("Daniil", "Osipov", "21", "MDBI")
David = student("David", "Barrero Gonzalez", "31", "MCSBT")
Edem = student("Edem", "Francois", "28", "MCSBT")
Eduardo =student("Eduardo", "Paraja", "23", "MDBI")
Florian = student("Florian", "Diegruber", "25", "MCSBT")
Hannah = student("Hannah", "Oldorf", "23", "MCBT")
Isabella =student("Isabella", "Rosenthal", "27", "MDBI")
Javier = student("Javier", "Fernandez", "24", "MCSBT")
Lukas = student ("Lukas", "Hauser", "28","MDBI")
Leila = student("Leila", "Tazi", "27", "MCSBT")
Laura = student("Laura", "Kageneck", "23", "MCSBT")
Monica = student("Monica", "Alvarenga","28", "MDBI")
Natalie=student("Natalie", "Cedeno", "26", "MDBI")
Octavio = student("Octavio", "Ramírez", "28", "MDBI")
Tancredi= student("Tancredi", "Bernard", "21", "MCSBT")
Yasmine= student("Yasmine", "Lyagoubi", "23", "MDBI")
Arthur = student("Arthur", "Maroquene-Froissart","23", "MCSBT")
Zineb=student("Zineb ", "Mezzour","22","MCSBT")
Felix = student("Felix ", "Fastrich", "23", "MDBI")


