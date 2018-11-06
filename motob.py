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
    
     def __init__(self,motors):
         self.motors = motors
         self.values = []


         
         
    #Receive a new motor recommendation, load it into the value slot, and operationalize it.
     def update(self, values): 
         self.values = values
         self.operationalize()
         
     #Motob får motor_recommendations fra Arbitrator
     #convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).    
     def operationalize(self):
        motor = Motors()
        #bruker 0.5 som duration til å begynne med, kan være at denne må endres

        motor.set_value(self.values, 0.5)
