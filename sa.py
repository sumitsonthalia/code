#!/usr/bin/python2
import os
import commands
import cgi
import cgitb
cgitb.enable()
print "Content-Type:text/html\r\n\n\r"
print 
x=cgi.FormContent()
pas=x['pass'][0]
uid=x['uname'][0]
l=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
if uid in l :
	print "location: http://192.168.234.132/upfail.html"
	print ch
else :
	os.system('sudo useradd '  +uid)
	os.system("echo " +pas+ " |sudo passwd " +uid+" --stdin" )
	print "Success"

