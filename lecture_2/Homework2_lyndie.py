
#####################################
# Title: Homework 2                 #
# Filename: Homework2_lyndie        #
# Original Author: Lyndie Mitchell  #
# Most Recent Edit: 2/21/2015       #
# Last Editor: Lyndie Mitchell      #
#####################################

from visual import *
from math import sqrt, pi
from const import E0
k=1.0/(4*pi*E0)

print 'Location of Charge: [m]'
q = [None,None,None,None]               #user must input information about the charge location
q[0] = float(raw_input ('x-coordinate='))
q[1] = float(raw_input ('y-coordinate='))
q[2] = float(raw_input ('z-coordinate='))
q[3] = float(raw_input ('Charge: [C]='))#python disagreed with inputing a decimal charge so I'm converting it to a float rather than an int
print q, '[m,C]'                        #double checking to make sure user entered what they wanted

print 'Location of calculation of field: [m]'
r = [None, None, None]                  #initial positions must be input
r[0] = float(raw_input ('x-coordinate=' ))
r[1] = float(raw_input ('y-coordinate='))
r[2] = float(raw_input ('z-coordinate='))
print r, '[m]'                          #double checking user entered what they wanted to
print' '                                #leaving extra space to make it easier to distinguish the answer from the rest of the input/output
mag = sqrt(((r[0]-q[0])**2) + ((r[1]-q[1])**2) + ((r[2]-q[2])**2))
E = [None, None, None]
E[0] = (k*q[3]*(r[0]-q[0]))/(mag**3)    #calculating the i component of the electric field
E[1] = (k*q[3]*(r[1]-q[1]))/(mag**3)    #calculating the j component of the electric field
E[2] = (k*q[3]*(r[2]-q[2]))/(mag**3)    #calculating the k component of the electric field
E_mag= sqrt(((E[0])**2)+((E[1])**2)+((E[2])**2))     #calculating the magnitude of the electric field
print 'E=', E, '[N/C]'
print '|E|=', E_mag, '[N/C]'




