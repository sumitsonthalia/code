#!/usr/bin/python2
import os
import getpass
import commands
import sys
import fileinput
import cgi
import cgitb

cgitb.enable()

print "Content-Type:text/html"
#print "location: http://192.168.234.132/download.html"
print	
print "hello"
cmd=commands.getstatusoutput("hostname -i")
if cmd[0]==0:
	k=cmd[1]
x=cgi.FormContent()
n=x['size'][0]
ch=x['cho'][0]
pas=x['pas'][0]
uid=x['uname'][0]
l=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
if uid in l :
	print "location: http://192.168.234.132/saasfa.html"
	print

elif ch == '1':
	ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= ce[1]:
		print
		print ce[1]+n
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system('sudo useradd '  +uid)
		os.system("sudo echo " +pas+ " | passwd " +pas+ " --stdin" )
		os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1 >>/var/www/html/gc.txt")
		os.system("sudo mkfs.vfat /dev/vg1/"+uid+" >>/var/www/html/gc.txt")
		os.system("sudo mkdir /staaso/"+uid)
		os.system("sudo mount /dev/vg1/"+uid+" /staaso/"+uid)
		f1=open('/etc/exports','a')
		f1.write("/staaso/"+uid+ " *(rw,no_root_squash)")
		f1.close()
		os.system("sudo /etc/init.d/nfs restart  >>/var/www/html/gc.txt")
		f1=open('/var/www/html/staasoclient','w+')
		f1.write("import os \nos.system('mkdir /media/rdbox')\nos.system('mount "+k+":/staaso/"+uid+" /media/rdbox')")
		f1.close()
		os.system('chmod +x staasoclient')		
elif ch == '2':
	ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= ce[1]:
		print		
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system('sudo useradd '  +uid)
		os.system("sudo echo " +pas+ " | passwd " +pas+ " --stdin" )
		os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1 >>/var/www/html/gc.txt")
		os.system("sudo mkfs.vfat /dev/vg1/"+uid+" >>/var/www/html/g1c.txt")
		os.system("sudo mkdir /staaso/"+uid)
		os.system("sudo mount /dev/vg1/"+uid+" /staaso/"+uid)
		os.system("sudo chown "+uid+ " /staaso/"+uid)
		os.system("sudo yum install sshfs -y >>/var/www/html/gc.txt")
		os.system("sudo service sshd restart >>/var/www/html/gc.txt")
		f1=open('/var/www/html/staasoclient','w+')
		f1.write("import os \nos.system('mkdir /media/rdbox')\nos.system('sshfs "+uid+"@"+k+":/staaso/"+uid+" /media/rdbox')")
		f1.close()
		os.system('sudo chmod +x staasoclient')			
		print	
elif ch == '3':
	os.system('sudo useradd  '  +uid)
	os.system("sudo echo " +pas+ " | passwd " +pas+ " --stdin " )
	os.system("sudo lvcreate --name "+uid+" --size "+str(n)+"G  vg1  >>/var/www/html/gc.txt")
	os.system("sudo yum install scsi-target-utils  >>/var/www/html/gc.txt")
	fi=open('/etc/tgt/target.conf','a')		
	fi.write("<target mystore"+uid+"> \n backing-store /dev/vg1/"+uid+"</target>")	
	fi.close()	
	os.system("sudo setenforce 0;sudo iptables -F;")
	os.system("sudo service tgtd restart  >>/var/www/html/gc.txt")
	fc=open('client','w+')
	fc.write("#!/usr/bin/python\nimport commands\niqn=commands.getoutput\(\"cat /etc/iscsi/initiatorname.iscsi |cut -d= -f2\"\)\nyum install iscsi-initiator-utils\niscsiadm --mode discoverydb --type sendtargets --portal "+k+" --discover;iscsiadm --mode node --targetname "+n+" --portal 192.168.1.1:3260 --login")
	fc.close()			
	print "UNDER CONSTRUCTION"
elif ch == "4" :
	ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= ce[1]:
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system("sudo lvextend --size "+str(n)+"G /dev/vg1/"+uid+ "  >>/var/www/html/gc.txt")
		os.system("sudo resize2fs /dev/vg1/"+uid+"  >>/var/www/html/gc.txt")
"""elif ch == "5" :
	os.system("sudo unmount  /dev/vg1/"+uid)
	os.system("sudo lvreduce --size "+str(n)+"G /dev/vg1/"+uid)
	os.system("sudo lvreduce --size "+str(n)+"G /dev/vg1/"+uid)
	os.system("sudo lvreduce --size "+str(n)+"G /dev/vg1/"+uid)
	os.system("sudo resize2fs /dev/vg1/"+uid)
"""
