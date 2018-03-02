#!/usr/bin/python
import os
import sys
print "Introduzca sus datos: "
usuario=raw_input("Introduzca el usuario: ")
password=raw_input("Introduzca contraseña: ")
basedatos=raw_input("Introduzca la base de datos a la que quier hacer un backup: ")
backup="mysql -u "+usuario+" -p"+password+" "+basedatos+ "| gzip > "+basedatos+".sql.gz"
os.system(backup)
print "listo"

