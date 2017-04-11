#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb
import crypt
cgitb.enable()

print "Content-type:text/html"
print
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
x=cgi.FormContent()
name=x['name'][0]
pas=x['pas'][0]
uid=x['uname'][0]
k=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
#print k
if uid in k :
	a=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f3")
	b=crypt.crypt(""+pas+"","$6$"+a+"$")
	if b == commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+" |cut -d: -f2") :
		os.system("sudo lvcreate --name snap"+uid+" --size 1G -s /dev/vg1/"+uid+" >>/var/www/html/gc.txt")
	else :
		print b
		print "Enter a VAlid pas"	
else:
	print "Enter a Valid USErname"
