import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
        ssh.connect('192.168.1.205', username='root', password='osd_SIP4321!')
except paramiko.SSHException:
        print("Connection Failed")
        quit()
#ssh.exec_command("su")
#stdin,stdout,stderr = ssh.exec_command("ansible -m ping all")
stdin,stdout,stderr = ssh.exec_command("ls -lrt /usr/src/")
for line in stdout.readlines():
        print(line.strip())
ssh.close()