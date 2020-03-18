# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:18:52 2020

@author: kaimo
"""

from io import open
import pickle

# =============================================================================
# Clase Personaje
# =============================================================================
class Personaje:
  __nombre  = ""
  __vida    = 0
  __ataque  = 0
  __defensa = 0
  __alcance = 0
  
  def __init__(self, nombre, vida, ataque, defensa, alcance):
    self.__nombre  = nombre
    self.__vida    = vida
    self.__ataque  = ataque
    self.__defensa = defensa
    self.__alcance = alcance
  
  # Informacion del personaje
  def __str__(self):
    return "{} :\t {} Vida | {} Ataque | {} Defensa | {} Alcance".format(self.__nombre, self.__vida, self.__ataque,self.__defensa, self.__alcance)
  
  def getNombre(self):
    return self.__nombre
  
# =============================================================================
# Clase Gestor 
# =============================================================================
class Gestor:
  personajes = []
  
  # Constructor de clase
  def __init__(self):
    self.cargar()
  
  def agregar(self,p):
    for personaje in self.personajes:   # Verificar si el personaje ya existe
      if personaje.getNombre() == p.getNombre():
        return
    self.personajes.append(p)
    self.guardar()
  
  def borrar(self,nombre):
    for personaje in self.personajes:   # Verificar si el personaje ya existe
      if personaje.getNombre() == nombre:
        self.personajes.remove(personaje)
        self.guardar()
        print("Personaje {} borrado.".format(nombre))
        return      
  
  def mostrar(self):
    if len(self.personajes) > 0:
      for p in self.personajes:
        print(p)
    else:
      print("El gestor está vacio")
      
  def cargar(self):
    fichero = open('personajes.pckl', 'ab+')  # Append binario, solo es escritura, y el + es para lectura
    fichero.seek(0)  # Apuntamos al inicio siempre
    try:  # Buscamos si hay peliculas adentro, considerando que el archivo pueda estar vacio
      self.personajes = pickle.load(fichero)  # Leer las peliculas
    except:
      #print("El fichero está vacio") 
      pass
    finally:
      fichero.close()
      print("Se han cargado {} personajes".format(len(self.personajes)))
    
  def guardar(self):
    fichero = open('personajes.pckl', 'wb')
    pickle.dump(self.personajes, fichero)
    fichero.close()
      
  """ #Destructor de clase: Se encarga de hacer un guardado de seguridad
  def __del__(self):
    self.guardar()  # Guardado automatico
    print("Se ha guardado el fichero")
  """

gestor = Gestor()
#gestor.mostrar()

# Agregar personaje
gestor.agregar( Personaje("Caballera", 4,2,4,2) )
gestor.agregar( Personaje("Guerrero", 2,4,2,4) )
gestor.agregar( Personaje("Arquero", 2,4,1,8) )

gestor.mostrar()

gestor.borrar('Caballera')
gestor.borrar('Arquero')

gestor.mostrar()
