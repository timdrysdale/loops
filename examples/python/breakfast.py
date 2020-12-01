#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 19:12:27 2020

@author: timothy.d.drysdale@gmail.com
"""

def eat(item):
	print("yum, I had %s"%item)

menu = ["bacon","eggs","tattie scone","black pudding", "beans", "coffee"]

for item in menu:	
    eat(item)
