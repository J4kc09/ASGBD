#!/usr/bin/python 
import MySQLdb ## Importa la libreria MySQLdb
##Si queremos especificar una base de datos pondriamos  db='nombrebasededatos')
bd=MySQLdb.connect( host='192.168.8.85' port =3306 , user='user', passwd='password')
cursor=bd.cursor()
cursor.execute("select @@hostname")
data=cursor.fetchone()
print "Nombre servidor %s" %data 
bd.close()