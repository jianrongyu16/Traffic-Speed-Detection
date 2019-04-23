import numpy as np
import math

#Definition of hyper parameters
Height = 1.4*9.98 #m
#Alpha = math.radians(110)
Beta = math.radians(73) #75 76
Psi = math.radians(5)  #20 19
UH = 1080 #pixels
UW = 1920 #pixels

#Constants
D = UH/2/math.tan(Beta/2)

# Calculate the speed of a vehicle between two frames
# Convert pixel coordinates ux,uy in the image frame to world coordinates x,y 
def CalSpeed(ux1, uy1, ux2, uy2, time):
    theta1 = Psi + Beta/2 + math.atan2(UH/2 -uy1, D)
    theta2 = Psi + Beta/2 + math.atan2(UH/2 -uy2, D)

    E1 = D / math.cos(Psi + Beta/2 - theta1)
    E2 = D / math.cos(Psi + Beta/2 - theta2)

    Gamma1 = math.atan2(ux1 - UW/2, E1)
    Gamma2 = math.atan2(ux2 - UW/2, E2)

    x1 = Height/math.cos(theta1) * math.tan(Gamma1)
    y1 = Height * math.tan(theta1)

    x2 = Height/math.cos(theta2) * math.tan(Gamma2)
    y2 = Height * math.tan(theta2)


    a = np.array((x1 ,y1))
    b = np.array((x2, y2))
    dis = np.linalg.norm(a-b)


    return dis/time


#print(CalSpeed(987,463, 1127, 658, 1.0))
#print('red truck in frame 148 178', CalSpeed(978,450, 1105, 635, 1.0)) #Red Truck 1
#print('white van in frame 148 178', CalSpeed(910,356, 973, 441, 1.0)) #White Van 1
#print('white van in frame 178 208',CalSpeed(  973, 441,1093, 619,1.0)) #White Van 2
#print('grey car in frame 208 238',CalSpeed( 993, 417, 1000, 553,1.0)) #Grey Car 1
#print('grey car in frame 238 268', CalSpeed( 1000, 553, 1160, 870,1.0)) #Grey Car 2
#print('Jeep car in frame 238 268',CalSpeed( 1036, 408, 1178, 520,1.0)) #Jeep
#
#print('the other way')
#print('suv in frame 218 238',CalSpeed( 1805, 424, 1610, 360,0.667)) #suv
#print('car in frame 240 270',CalSpeed( 1843, 483, 1500, 365,1.0)) #Jeep