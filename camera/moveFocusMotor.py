#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor, Evetar_FocusMotor

import time
import atexit
import argparse

import sys

def gotofocuspos(position):
    status,loc=ev.queryPos()
    diff = loc - position
    if diff < 0:
        ev.moveBackward(abs(diff))
    elif diff > 0:
        ev.moveForward(abs(diff))
    else:
        b = 0
print sys.argv[1:]

inputs=sys.argv[1:]

motorId=1

if(len(inputs) !=2):
	print("did not get enough arguments, must specify motor ID of 1 or 2 and number of steps")
	print("For example python moveFocusMotor.py 2 -50")
	
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


steps=int(inputs[1])
if (steps==0):
	status, loc = ev.queryPos()
	print("Current Position: "+str(loc))
	gotofocuspos(0)
	quit()
elif (steps<0):
	motorDir='backward'
else:
	motorDir='forward'
steps=abs(steps)
#print("I will move motor "+str(motorId)+" "+str(steps)+" steps "+motorDir)

# create a default object, no changes to I2C address or frequency
#mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
#def turnOffMotors():
#	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(3)un(Adafruit_MotorHAT.RELEASE)
#	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

#atexit.register(turnOffMotors)


#myStepper1 = mh.getStepper(200, motorId)  	# 200 steps/rev, motor port #1




#myStepper1.setSpeed(100)  		# 30 RPM




#print("Double coil steps")

#what we originally used
if (motorDir=='forward'):
    ev.moveBackward(steps)
else:
    ev.moveForward(steps)





