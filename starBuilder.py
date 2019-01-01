"""
Generates stars for use in solar system creation
"""

import random
import math
def habitableStar():
    mass = round(random.uniform(0.6,1.4),4)
    diameter = round(mass**0.74,4)
    surfaceTemp = round(5778*mass**0.505,4)
    lifeTime = round(mass**-2.5,4)
    brightness = round(mass**3,4)
    hz = round(math.sqrt(brightness),4)
    ib = round(hz*0.95,4)
    ob = round(hz*1.37,4)

    if surfaceTemp <= 5200:
        color = "yellowOrange"
    elif surfaceTemp <= 6000:
        color = "yellowWhite"
    else: 
        color = "white"
    return mass, diameter, surfaceTemp, lifeTime, brightness, hz, ib, ob, color;
    
def randomStar():
    mass = round(random.uniform(0.09,140),4)
    diameter = round(mass**0.74,4)
    surfaceTemp = round(5778*mass**0.505,4)
    lifeTime = round(mass**-2.5,4)
    brightness = round(mass**3,4)
    hz = round(math.sqrt(brightness),4)
    ib = round(hz*0.95,4)
    ob = round(hz*1.37,4)

    if surfaceTemp <= 3700:
        color = "orangeRed"
    elif surfaceTemp <= 5200:
        color = "yellowOrange"
    elif surfaceTemp <= 6000:
        color = "yellowWhite"
    elif surfaceTemp <= 7500:
        color = "white"
    elif surfaceTemp <= 10000:
        color = "whiteBlue"
    elif surfaceTemp <= 33000:
        color = "blueWhite"
    else: 
        color = "blue"
    return mass, diameter, surfaceTemp, lifeTime, brightness, hz, ib, ob, color;
    
if __name__ == "__main__":
    star = habitableStar()
    outFile = open("livingStar.txt","w")
    for item in star:
        outFile.write(str(item) + "\n")
    outFile.close()
    outFile = open("regularStar.txt","w")
    star = randomStar()
    for item in star:
        outFile.write(str(item) + "\n")  
    outFile.close()
    