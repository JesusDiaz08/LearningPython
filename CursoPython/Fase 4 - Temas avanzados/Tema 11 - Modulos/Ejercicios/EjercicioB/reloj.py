# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:54:55 2020

@author: kaimo
"""

import datetime
import time
import os

while True:
  os.system("cls")
  dt = datetime.datetime.now()  # Importamos la hora actual
  print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
  
  # Pausamos el bucle durante un segundo
  time.sleep(1)


