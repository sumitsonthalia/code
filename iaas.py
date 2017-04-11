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
vcp=x['vcpu'][0]
hd=x['hd'][0]
ram=x['ram'][0]
pas=x['pas'][0]
uid=x['uname'][0]
ce=commands.getstatusoutput("sudo vgdisplay vg1|grep Free|cut -d' ' -f16")
if hd >= ce[1]:
	print
	print ce[1]+hd
	print "SORY WE DONT HAVE ENOUGH RESOURCE TRY AMAZON"
else :
	os.system('sudo useradd '  +uid)
	os.system("sudo echo " +pas+ " |sudo passwd " +uid+ " --stdin >>/var/www/html/gc.txt" )
	os.system("sudo lvcreate --name "+uid+" --size "+str(hd)+"G  vg1 >>/var/www/html/gc.txt")
	f1=open('/etc/exports','w+')
	f1.read()
	f1.write("/dev/vg1/"+uid+ " *(rw,no_root_squash)")
	f1.close()
	os.system("sudo /etc/init.d/nfs restart  >>/var/www/html/gc.txt")
	f1=open('/var/www/html/iaasclient','w+')
	f1.write("import os \nos.system('mkdir /media/rdbox')\nos.system('mount "+k+":/staaso/"+uid+" /media/rdbox')")
	f1.close()
	os.system('sudo chmod +x /var/www/html/iaasclient')	
	if ch == '1':
		os.system("mkdir /myos")
		os.system("touch new"+uid+".img")
		os.system('sudo virt-install --name='+name+' --ram='+ram+' --vcpu='+vcp+' --cdrom=/root/Desktop/.iso --os-type = win7 --os-variant= windows --disk path=/dev/vg1/'+uid+',size='+hd+' --extra-args=')
	elif ch == '2':
		os.system("sudo virt-install --name="+name+" --ram="+ram+" --vcpu="+vcp+" --cdrom=/root/Desktop/rhel-server-7.0-x86_64-dvd.iso --os-type = linux --os-variant= rhel7 --disk path=/dev/vg1/"+uid+",size="+hd+" --extra-args= 'ks=/root/Desktop/rhel7.cfg' --noautoconsole")
	elif ch == '3':
		os.system('sudo virt-install --name='+name+' --ram='+ram+' --vcpu='+vcp+' --location=http://instructor.example.com/pub/rhel6/dvd --os-type=linux --os-variant=rhel6 --disk path=/dev/vg1/'+uid+',size='+hd+' --graphics vnc,listen=0.0.0.0,port=5910 --extra-args="ks=ftp://192.168.0.198/pub/ks.cfg" --noautoconsole')
		f1=open('/var/www/html/client','w+')
		f1.write("#!/usr/bin/python2 \nimport os\nos.system('vncviewer "+k+":5910')")
