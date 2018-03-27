#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor, Evetar_FocusMotor

import time
import atexit
import argparse

import sys

print sys.argv[1:]

inputs=sys.argv[1:]

motorId=1

if(len(inputs) !=1):
	print("did not get enough arguments, must specify motor ID of 1 or 2")
	print("For example python resetFocusMotor.py 2 ")
	
	exit()

if(inputs[0]=='1'):
    ev = Evetar_FocusMotor(30)
    motorId=1
elif(inputs[0]=='2'):
    ev=Evetar_FocusMotor(31)
    motorId=2
elif(inputs[0]=='3'):
    ev=Evetar_FocusMotor(32)
    motorId=3
else:
    print("incorrect motor indexing used")
    exit()        



ev.resetMotor()





