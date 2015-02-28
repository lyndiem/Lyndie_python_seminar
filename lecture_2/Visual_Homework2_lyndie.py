
#####################################
# Title: Homework 2                 #
# Filename: Visual_Homework2_lyndie #
# Original Author: Lyndie Mitchell  #
# Most Recent Edit: 2/23/2015       #
# Last Editor: Lyndie Mitchell      #
#####################################

from visual import *
from math import sqrt, pi
from const import E0
k=1.0/(4*pi*E0)
a=0.5

#   Well, the code works. Pass. I'd recommend you make the arrows small enough to reasonably match
#   the charges, though that's admittedly the fault of the value assigned in the homework. I'm
#   a fan of the different colors, and the way you used your other script as a base for this one.
#   I'll bet that sped you up a lot. Remember, this part of the homework is to let you see something
#   that will improve your intuition. If you can think of a thing or two to visualize that you think
#   would be interesting or informative, feel free to add it as long as it doesn't interfere with the
#   assigned visualization.

q_p = [0, a, 0, 4*pi*E0]          #Can't enter values like 4piE0 so for the visualization assignment I'm just assigning the value now
q_n = [0,-a, 0, -4*pi*E0]
#print q_p, '[m, m, m, C]'                          #double checking to make sure user entered what they wanted

#print 'Location of calculation of field: [m]'
r0 = [0, 0, 0]
r1 = [a, 0, 0]
r2 = [0, 0, -a]
r3 = [-a, 0, 0]
r4 = [0, 0, a]
#print r, '[m]'                          #double checking user entered what they wanted to
#print' '                                #leaving extra space to make it easier to distinguish the answer from the rest of the input/output

mag0_p = sqrt(((r0[0]-q_p[0])**2) + ((r0[1]-q_p[1])**2) + ((r0[2]-q_p[2])**2))
E0_p = [None, None, None]
E0_p[0] = (k*q_p[3]*(r0[0]-q_p[0]))/(mag0_p**3)    #calculating the i component of the electric field
E0_p[1] = (k*q_p[3]*(r0[1]-q_p[1]))/(mag0_p**3)    #calculating the j component of the electric field
E0_p[2] = (k*q_p[3]*(r0[2]-q_p[2]))/(mag0_p**3)    #calculating the k component of the electric field


mag0_n = sqrt(((r0[0]-q_n[0])**2) + ((r0[1]-q_n[1])**2) + ((r0[2]-q_n[2])**2))
E0_n = [None, None, None]
E0_n[0] = (k*q_n[3]*(r0[0]-q_n[0]))/(mag0_n**3)    #calculating the i component of the electric field
E0_n[1] = (k*q_n[3]*(r0[1]-q_n[1]))/(mag0_n**3)    #calculating the j component of the electric field
E0_n[2] = (k*q_n[3]*(r0[2]-q_n[2]))/(mag0_n**3)
E_0 = [(E0_p[0])+E0_n[0], E0_p[1]+E0_n[1], E0_p[2]+E0_n[2]]
print 'Origin', E_0 

mag1_p = sqrt(((r1[0]-q_p[0])**2) + ((r1[1]-q_p[1])**2) + ((r1[2]-q_p[2])**2))
E1_p = [None, None, None]
E1_p[0] = (k*q_p[3]*(r1[0]-q_p[0]))/(mag1_p**3)    #calculating the i component of the electric field
E1_p[1] = (k*q_p[3]*(r1[1]-q_p[1]))/(mag1_p**3)    #calculating the j component of the electric field
E1_p[2] = (k*q_p[3]*(r1[2]-q_p[2]))/(mag1_p**3)    #calculating the k component of the electric field
#E_mag= sqrt(((E[0])**2)+((E[1])**2)+((E[2])**2))     #calculating the magnitude of the electric field
#print 'E1_p=', E1_p, '[N/C]'
#print '|E|=', E_mag, '[N/C]'

mag1_n = sqrt(((r1[0]-q_n[0])**2) + ((r1[1]-q_n[1])**2) + ((r1[2]-q_n[2])**2))
E1_n = [None, None, None]
E1_n[0] = (k*q_n[3]*(r1[0]-q_n[0]))/(mag1_n**3)    #calculating the i component of the electric field
E1_n[1] = (k*q_n[3]*(r1[1]-q_n[1]))/(mag1_n**3)    #calculating the j component of the electric field
E1_n[2] = (k*q_n[3]*(r1[2]-q_n[2]))/(mag1_n**3)
E1 = [(E1_p[0])+E1_n[0], E1_p[1]+E1_n[1], E1_p[2]+E1_n[2]]
print r1, E1 

mag2_p = sqrt(((r2[0]-q_p[0])**2) + ((r2[1]-q_p[1])**2) + ((r2[2]-q_p[2])**2))
E2_p = [None, None, None]
E2_p[0] = (k*q_p[3]*(r2[0]-q_p[0]))/(mag2_p**3)    #calculating the i component of the electric field
E2_p[1] = (k*q_p[3]*(r2[1]-q_p[1]))/(mag2_p**3)    #calculating the j component of the electric field
E2_p[2] = (k*q_p[3]*(r2[2]-q_p[2]))/(mag2_p**3)    #calculating the k component of the electric field


mag2_n = sqrt(((r2[0]-q_n[0])**2) + ((r2[1]-q_n[1])**2) + ((r2[2]-q_n[2])**2))
E2_n = [None, None, None]
E2_n[0] = (k*q_n[3]*(r2[0]-q_n[0]))/(mag2_n**3)    #calculating the i component of the electric field
E2_n[1] = (k*q_n[3]*(r2[1]-q_n[1]))/(mag2_n**3)    #calculating the j component of the electric field
E2_n[2] = (k*q_n[3]*(r2[2]-q_n[2]))/(mag2_n**3)
E_2 = [(E2_p[0])+E2_n[0], E2_p[1]+E2_n[1], E2_p[2]+E2_n[2]]
print r2, E_2

mag3_p = sqrt(((r3[0]-q_p[0])**2) + ((r3[1]-q_p[1])**2) + ((r3[2]-q_p[2])**2))
E3_p = [None, None, None]
E3_p[0] = (k*q_p[3]*(r3[0]-q_p[0]))/(mag3_p**3)    #calculating the i component of the electric field
E3_p[1] = (k*q_p[3]*(r3[1]-q_p[1]))/(mag3_p**3)    #calculating the j component of the electric field
E3_p[2] = (k*q_p[3]*(r3[2]-q_p[2]))/(mag3_p**3)    #calculating the k component of the electric field


mag3_n = sqrt(((r3[0]-q_n[0])**2) + ((r3[1]-q_n[1])**2) + ((r3[2]-q_n[2])**2))
E3_n = [None, None, None]
E3_n[0] = (k*q_n[3]*(r3[0]-q_n[0]))/(mag3_n**3)    #calculating the i component of the electric field
E3_n[1] = (k*q_n[3]*(r3[1]-q_n[1]))/(mag3_n**3)    #calculating the j component of the electric field
E3_n[2] = (k*q_n[3]*(r3[2]-q_n[2]))/(mag3_n**3)
E_3 = [(E3_p[0])+E3_n[0], E3_p[1]+E3_n[1], E3_p[2]+E3_n[2]]
print r3, E_3

mag4_p = sqrt(((r4[0]-q_p[0])**2) + ((r4[1]-q_p[1])**2) + ((r4[2]-q_p[2])**2))
E4_p = [None, None, None]
E4_p[0] = (k*q_p[3]*(r4[0]-q_p[0]))/(mag4_p**3)    #calculating the i component of the electric field
E4_p[1] = (k*q_p[3]*(r4[1]-q_p[1]))/(mag4_p**3)    #calculating the j component of the electric field
E4_p[2] = (k*q_p[3]*(r4[2]-q_p[2]))/(mag4_p**3)    #calculating the k component of the electric field


mag4_n = sqrt(((r4[0]-q_n[0])**2) + ((r4[1]-q_n[1])**2) + ((r4[2]-q_n[2])**2))
E4_n = [None, None, None]
E4_n[0] = (k*q_n[3]*(r4[0]-q_n[0]))/(mag4_n**3)    #calculating the i component of the electric field
E4_n[1] = (k*q_n[3]*(r4[1]-q_n[1]))/(mag4_n**3)    #calculating the j component of the electric field
E4_n[2] = (k*q_n[3]*(r4[2]-q_n[2]))/(mag4_n**3)
E_4 = [(E4_p[0])+E4_n[0], E4_p[1]+E4_n[1], E4_p[2]+E4_n[2]]
print r4, E_4

pos=sphere(pos=vector(0,a,0), radius=0.25, color=color.red)
neg=sphere(pos=vector(0,-a,0), radius=0.25, color=color.blue)

Evector_0=arrow(pos=vector(r0), axis=vector(E_0[0], E_0[1], E_0[2]), shaftwidth=0.1, color=color.cyan)
Evector_1=arrow(pos=vector(r1), axis=vector(E1[0], E1[1], E1[2]), shaftwidth=0.1, color=color.green)
Evector_2=arrow(pos=vector(r2), axis=vector(E_2[0], E_2[1], E_2[2]), shaftwidth=0.1, color=color.magenta)
Evector_3=arrow(pos=vector(r3), axis=vector(E_3[0], E_3[1], E_3[2]), shaftwidth=0.1, color=color.orange)
Evector_4=arrow(pos=vector(r4), axis=vector(E_4[0], E_4[1], E_4[2]), shaftwidth=0.1, color=color.yellow)

print'Origin', (Evector_0.axis)
print r1, (Evector_1.axis)
print r2, (Evector_2.axis)
print r3, (Evector_3.axis)
print r4, (Evector_4.axis)



