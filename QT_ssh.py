import paramiko
class QT_ssh:
    def qt_ssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect('192.168.1.50', username='root', password='osd_SIP4321!')
        except paramiko.SSHException:
            print("Connection Failed")
            quit()
        #ssh.exec_command("su")
        #stdin,stdout,stderr = ssh.exec_command("ansible -m ping all")
        stdin,stdout,stderr = ssh.exec_command("/bin/cat /etc/asterisk/extensions_custom.conf")

        for line in stdout.readlines():
            list_ssh = []
            list_ssh = line.strip("\n")
            print(list_ssh)

            #print(line.strip(line))

        ssh.close()

res = QT_ssh()
res.qt_ssh()