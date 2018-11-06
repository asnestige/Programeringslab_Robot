#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:01:00 2018

@author: NinaAarvik
"""
from motors import Motors

#Behavior sender recommendations til Arbitraty, som bestemmer hvilken handling som er av høyest prioritet. 
#Det sendes da en ny recommendation til motob, som kun utfører den recommendation-en den får fra Arbitrator. 
#bbcon er overordnet oversikt. 

class Motob: 
    
     def __init__(self):
         self.motors = Motors()
         self.values = []


         
         
    #Receive a new motor recommendation, load it into the value slot, and operationalize it.
     def update(self, values): 
         self.values = values[0]
         print("values listen fra motors")
         print (self.values)
         self.operationalize()
         
     #Motob får motor_recommendations fra Arbitrator
     #convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).    
     def operationalize(self):

        if self.values[0] == 0.5 and self.values[1] == 0.5:
            self.motors.forward(0.25, 0.5)

        if self.values[0] == 0 and self.values[1] == 0:
            self.motors.stop()

        if self.values[0] == -0.5 and self.values[1] == 1:
            self.motors.left(0.25, 0.5)

        if self.values[0] == 1 and self.values[1] == -0.5:
            self.motors.left(0.25, 0.5)


