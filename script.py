#!/usr/bin/python
import os
import sys
usuario=sys.argv[1]
contrasena=sys.argv[2]
basedatos=sys.argv[3]
acceso="mysql -u "+usuario+" -p"+contrasena+" "+basedatos
os.system(acceso)
