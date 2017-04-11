#!/usr/bin/python2
import crypt
import commands
import cgi
print "Content-type: text/html"
print
x=cgi.FormContent()
uid=x['uname'][0]
pas=x['pass'][0]
k=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
#print k
if uid in k :
	a=commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+"|cut -d: -f2|cut -d$ -f3")
	b=crypt.crypt(""+pas+"","$1$"+a+"$")
	if b == commands.getoutput("sudo cat /etc/shadow|grep -w "+uid+" |cut -d: -f2") :
		print "auth"
	else :
		print b
		print "Enter a VAlid pas"	
else:
	print "Enter a Valid USErname"
