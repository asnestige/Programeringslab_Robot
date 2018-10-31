#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:01:00 2018

@author: NinaAarvik
"""
from motors import Motors

class Motob: 
    
     def __init__(self,motors):
         self.motors = motors 
         self.values = []
         
         
    #Receive a new motor recommendation, load it into the value slot, and operationalize it.
     def update(self, values): 
         self.values = values 
         self.operationalize() 
         
         
     #convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).    
     def operationalize(self):
                 