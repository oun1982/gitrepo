import paramiko
 
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('192.168.66.111', username='oun1982', password='osd_SIP4321!')
except paramiko.SSHException:
        print ("Connection Failed")
        quit()
#ssh.exec_command("su")
#stdin,stdout,stderr = ssh.exec_command("ansible -m ping all")
stdin,stdout,stderr = ssh.exec_command("find / -name *.conf")
for line in stdout.readlines():
        print(line.strip())
ssh.close()