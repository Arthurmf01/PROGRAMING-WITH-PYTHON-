#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:21:36 2018

@author: arthurmaroquenefroissart
"""

#%%

#Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.


from flask import Flask, jsonify

server = Flask("phonebookmanager")

phonebook = {"mum":"0687678977","dad":"0684777750","ulysse":"0678564535"}

@server.route("/add_contact/<name>/<phone>")
def add_contact(name,phone): 
    phonebook[name] = phone   
    return jsonify("Congrats ! The contact " + name + " has been added to contacts repertory")

@server.route("/get_contact/<name>")
def get_contact(name): 
    phone = phonebook[name]   
    return jsonify("The phone number for the contact " + name + " is " + phone)

@server.route("/delete_contact/<name>")
def delete_contact(name): 
    phonebook.pop(name)
    return jsonify("You have delete the contact " + name + " from your contacts repertory")

@server.route("/update_contact/<name>/<phone>")
def update_contact(name,phone): 
    phonebook[name] = phone   
    return jsonify("Congrats ! You have changed the following phone number for " + name + " to " + phone)

@server.route("/phonebook")
def show_phonebook():
    return jsonify(phonebook)


server.run()