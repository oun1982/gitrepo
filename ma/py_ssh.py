import paramiko
import socket

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('192.168.1.205', username='root', password='osd_SIP4321!')
except paramiko.SSHException:
        print("Connection Failed")
        quit()
#ssh.exec_command("su")
#stdin,stdout,stderr = ssh.exec_command("ansible -m ping all")
name = stdin,stdout,stderr = ssh.exec_command("hostname")
for hname in stdout.readlines():
        hostname = hname

stdin,stdout,stderr = ssh.exec_command("df -h")
res = ''
for line in stdout.readlines():
        res += line
        #print(line.strip())

ssh.close()