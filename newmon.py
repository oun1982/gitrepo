import paramiko, socket
from fpdf import FPDF
class Mainmon:
    def __init__(self, host):
        ip = host
        res = ' '
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, username='root', password='osd_SIP4321!')
        except paramiko.SSHException:
            print("Connection Failed")
            quit()

        name = stdin,stdout,stderr = ssh.exec_command("hostname")
        for hname in stdout.readlines():
            hostname = hname

        stdin,stdout,stderr = ssh.exec_command("df -h")

        for line in stdout.readlines():
            res += line
        ssh.close()
        self.showReport(res, hostname)

    def showReport(self, res, hostname):
        df = res.split(' ')
        list1 = [e for e in df if e]
        df_res = ('Name: Total %s  |  Avaliable %s  |  Used %s  |  Used in Percent %s'%(list1[7] ,list1[8] ,list1[9], list1[10]))
        symbol = '-' * 200
        pcent = int((list1[10]).replace('%',''))

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        if pcent > 90:
            pdf.set_text_color(254, 0, 0)
        pdf.cell(100, 10, txt=symbol, ln=1, align="C")
        pdf.cell(200, 10, txt=hostname, ln=1, align="C")
        pdf.cell(120, 10, txt=df_res, ln=1, align="C")
        pdf.cell(100, 10, txt=symbol, ln=1, align="C")
        pdf.output("df.pdf")

mon = Mainmon('192.168.1.205')
mon = Mainmon('192.168.1.220')
