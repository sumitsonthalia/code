#!/usr/bin/python2
import cgi
import commands
print "Content-Type:text/html"
x=cgi.FormContent()
ch=x['choice'][0]
pas=x['pass'][0]
uid=x['uname'][0]
k=commands.getoutput("sudo cat /etc/shadow|cut -d: -f1")
if uid in k :
	print "location: http://192.168.234.132/saasfa.html"
	print
elif ch == '1':
	ce=commands.getstatusoutput("vgdisplay vg1|grep Free|cut -d' ' -f16")
	n=float(raw_input("Enter the required size in GB"))
	if n >= float(ce[1]):
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		uid=raw_input('Enter User Name')
		pas=getpass.getpass('Enter Password')
		os.system('useradd '  +uid)
		os.system("echo " +pas+ " | passwd " +pas+ " --stdin" )
		os.system("lvcreate --name "+uid+" --size "+str(n)+"G  vg1")
		os.system("mkfs.vfat /dev/vg1/"+uid)
		os.system("mkdir /staaso/"+uid)
		os.system("mount /dev/vg1/"+uid+" /staaso/"+uid)
		f1=open('/etc/exports','w+')
		f1.read()
		f1.write("/staaso/"+uid+ " *(rw,no_root_squash)")
		f1.close()
		os.system("/etc/init.d/nfs restart")
		f1=open('staasoclient','w+')
		f1.write("import os \nos.system('mkdir /media/rdbox')\nos.system('mount "+k+":/staaso/"+uid+" /media/rdbox')"
		f1.close()
		os.system('chmod +x staasoclient')			
		break
elif ch == '2':
	ce=commands.getstatusoutput("vgdisplay vg1|grep Free|cut -d' ' -f16")
	n=float(raw_input("Enter the required size in GB"))
	if n >= float(ce[1]):
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		uid=raw_input('Enter User Name')
		pas=getpass.getpass('Enter Password')
		os.system('useradd -s /usr/bin/firefox  '  +uid)
		os.system("echo " +pas+ " | passwd " +pas+ " --stdin" )
		os.system("lvcreate --name "+uid+" --size "+str(n)+"G  vg1")
		os.system("mkfs.vfat /dev/vg1/"+uid)
		os.system("mkdir /staaso/"+uid)
		os.system("mount /dev/vg1/"+uid+" /staaso/"+uid)
		os.system("chown "+uid+ " /staaso/"+uid)
		os.system("yum install sshfs -y")
		os.system("service sshd restart")
		f1=open('staasoclient','w+')
		f1.write("import os \nos.system('mkdir /media/rdbox')\nos.system('sshfs "+uid+"@"+k+":/staaso/"+uid+" /media/rdbox')")
		f1.close()
		os.system('chmod +x staasoclient')			
		break	
elif ch == '3':
	os.system('useradd  '  +uid)
	os.system("echo " +pas+ " | passwd " +pas+ " --stdin" )
	os.system("lvcreate --name "+uid+" --size "+str(n)+"G  vg1")
	os.system("yum install scsi-target-utils")
	fi=open('/etc/tgt/target.conf','w+')		
	fi.read()
	fi.write("<target mystore"+uid+"> \n backing-store /dev/vg1/"+uid+"</target>")	
	fi.close()	
	os.system("setenforce 0;iptables -F;")
	os.system("yum install scsi-target-utils")
	os.system("mount /dev/vg1/"+uid+" /staaso/"+uid)
	os.system("service tgtd restart")
	fc=open('CLient'+uid,'w+')
	fc.write("")
	fc.close()			
	print "UNDER CONSTRUCTION"
elif ch == "4" :
	ce=commands.getstatusoutput("vgdisplay vg1|grep Free|cut -d' ' -f16")
	if n >= float(ce[1]):
		print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
	else :
		os.system("lvextend --size "+str(n)+"G /dev/vg1/"+uid)
		os.system("resize2fs /dev/vg1/"+uid)
