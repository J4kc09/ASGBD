#!/usr/bin/python
import os
import sys
print "Introduzca usuario"
usuario=raw_input()
print "Introduzca clave"
contrasena=raw_input()
print "Introduzca nombre de la base de datos"
basedatos=raw_input()
acceso="mysql -u "+usuario+" -p"+contrasena+" "+basedatos
os.system(acceso)
