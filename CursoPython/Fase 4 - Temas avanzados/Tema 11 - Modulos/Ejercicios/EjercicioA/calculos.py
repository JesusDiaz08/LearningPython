# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:48:06 2020

@author: kaimo
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:47:20 2020

@author: kaimo
"""

from operaciones import *

a, b, c, d = (10, 5, 0, "Hola")

print( "{} + {} = {}".format(a, b, suma(a, b) ) )
print( "{} - {} = {}".format(b, d, resta(b, d) ) )
print( "{} * {} = {}".format(b, b, producto(b, b) ) ) 
print( "{} / {} = {}".format(a, c, division(a, c) ) )
