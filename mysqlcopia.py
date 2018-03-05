#!/usr/bin/python

import os
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("-equipo", action="store", type=str)
parser.add_argument("-user", action="store", type=str)
parser.add_argument("-clave", action="store", type=str)
parser.add_argument("-bd", action="store", type=str)

args = parser.parse_args(sys.argv[1:])

os.system('mysqldump -h' + args.equipo + '--user' + args.user + '--password=' + args.clave + args.bd + '>backup.sql')

print "Backup completado"
