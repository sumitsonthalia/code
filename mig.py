#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb
cgitb.enable()

print "Content-type:text/html"
print
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
x=cgi.FormContent()
ch=x['cho'][0]
name=x['name'][0]
pas=x['pas'][0]
uid=x['uname'][0]
os.system("")
