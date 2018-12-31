"""
Generates stars for use in solar system creation
"""

import random
import math

mass = round(random.uniform(0.6,1.4),4)
diameter = round(mass**0.74,4)
surfaceTemp = round(mass**0.505,4)
lifeTime = round(mass**-2.5,4)
brightness = round(mass**3,4)
