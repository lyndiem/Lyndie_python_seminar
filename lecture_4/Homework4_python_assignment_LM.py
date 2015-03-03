########################################
#Title: Homework4_python_assignment_LM #
#Author: Lyndie Mitchell               #
#Last Edit: 3/3/2015                   #
########################################
NEED ACCUMULATOR VARIABLE

from math import sqrt, pi                               # Gather constants and functions
E0 = 8.854187817e-12 
k = 1.0 / (4 * pi * E0)

def E(q, P):
    r = (P[0] - q[0], P[1] - q[1], P[2] - q[2])
    mag = sqrt((r[0]**2) + (r[1]**2) + (r[2]**2))
    field = []
    field.append(k * (r[0] / mag) * (q[3] / (mag**2)))  # Calculate x, y, and z components
    field.append(k * (r[1] / mag) * (q[3] / (mag**2)))
    field.append(k * (r[2] / mag) * (q[3] / (mag**2)))
    return field
def F(E, q2):
    E=E(q,P)
    force = []
    force.append (E[0]*q2[3])
    force.append (E[1]*q2[3])
    force.append (E[2]*q2[3])
    return force
                  
q=[0,0,0,10**-6]                    #location of the charge

F=0.0
E(q,P) = 0.0
y=0
x=0
for i in range(0,51):               #dividing it up into 50 pieces of equal size, must be 50+1 to include the endpoint
    dy = 2.0/50                     #infinitesimal thickness in y of each piece is total length divided by # of pieces
    y = -1 + i*dy
    for j in range (0,51):
        dx = 2.0/50                 # same number of pieces as in the y calculation
        x = -1 + j*dx               #same as in y 
        #print "i=",i,"j=", j       #checking to see if nested loop works
        P=[x,y,1]                   # taking P as varying across dy and dx to sum up all of E(q,p)
        Flux = E(q,P)[2]*dx*dy      #flux due to the ball is the double integral of the z component of the electric field of the ball (x,y cancel out by symmetry) times dA (dx*dy).
        q2 = [x, y, 1, (10**-3)*dx*dy]   #the charge varies as we move across our little pieces and has value sigma*dx*dy and is constantly at z=1
print 'Flux =', Flux, '[Nm^2/C]'
print 'Force =', F, '[N]'           #I don't know why this isn't working but I may not have time to figure it out before class today. 


