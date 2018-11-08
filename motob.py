#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 11:01:00 2018

@author: NinaAarvik
"""
from motors import Motors
#from time import sleep

#Behavior sender recommendations til Arbitraty, som bestemmer hvilken handling som er av høyest prioritet. 
#Det sendes da en ny recommendation til motob, som kun utfører den recommendation-en den får fra Arbitrator. 
#bbcon er overordnet oversikt. 

class Motob: 
    
     def __init__(self, motors):
         self.motors = motors
         self.values = []         
         
    #Receive a new motor recommendation, load it into the value slot, and operationalize it.
     def update(self, values): 
         self.values = values # Henter den første listen i motor recommendation
         print("values listen fra motors")
         print (self.values)
         self.operationalize()
         
     #Motob får motor_recommendations fra Arbitrator
     #convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).    
     def operationalize(self):
        #Oppretter motors-objekt
        m = Motors()
        #henter inn recommendation fra arbitrator og plugger inn i motors
        m.set_value(self.values, 0.5)
        
        #Går gjennom listen og bruker den til å utføre de forskjellige handlingene fra motors
        for i in range(len(self.motors)):
            self.motors[i].set_value(self.values, 0.5)
         
         
"""
        if self.values[0] == 0.5 and self.values[1] == 0.5:
            m.forward(0.25, 0.5)
            print("forward")
        if self.values[0] == 0 and self.values[1] == 0:
            m.stop()
            print("stop!")
        if self.values[0] == -0.5 and self.values[1] == 1:
            m.left(0.25, 0.5)
            print("left")
        if self.values[0] == 1 and self.values[1] == -0.5:
            m.right(0.25, 0.5)
            print("right")
            
        #else: 
         #   self.motors.forward(0.25, 0.5)
            
        #sleep(1)

""" 
