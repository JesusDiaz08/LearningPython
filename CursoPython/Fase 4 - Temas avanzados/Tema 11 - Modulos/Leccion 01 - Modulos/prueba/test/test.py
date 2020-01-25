# Importar el directorio saludos
# import saludos;
# saludos.saludar()
# saludos.Saludo()
#from saludos import saludar, Saludo
#saludar() # Nos va a marcar error, ya que no se va a encontrar en el path, para ello hacemos los sig
#Saludo()

import sys
sys.path.insert(1, "..")  # ".." hace referencia al sistema anterior (/prueba)
# print(sys.path) # Nos da los directorios donde nuestro interprete de python,
                # desde el cual empieza a buscar para encontrar el modulo
# Al hacer el codigo de la linea 10, ahora podemos ejecutar sin problema el codigo de la linea 5-7
from saludos import saludar, Saludo
saludar() # Nos va a marcar error, ya que no se va a encontrar en el path, para ello hacemos los sig
Saludo()
