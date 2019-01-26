"""
Generates star system to be populated with planets.
"""

from starBuilder import habitableStar
from starBuilder import randomStar
import math
import random

def habitableSystem():
    star = habitableStar()
    innerBound = 0.1 * star[0]
    outerBound = 40 * star[0]
    frostLine = 4.85 * smath.sqrt(star[4])
    innerHabit = star[6]
    outerHabit = star[7]
    
    largestGass = frostLine + round(random.uniform(0.5,1.5),3)
    