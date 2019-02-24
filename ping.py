import time
import subprocess
lan_host = "192.168.66.254"
wan_host = "google.co.th"
#ping = call(["host",shell=True])
#ping = call(["ping", host , "-c", "2"])
def ping_func(host):
        datetime = time.strftime("-------------------------- %Y%m%d_%H%M --------------------------")
        #date_out = subprocess.Popen(["date"], stdout=subprocess.PIPE).communicate()
        #res_out = str(date_out)
        #ping_out = subprocess.Popen(["/bin/ping", host , "-c", "3"], stdout=subprocess.PIPE).communicate()
        ping_out = subprocess.Popen("/bin/ping " + host + " -c 15", shell=True, stdout=subprocess.PIPE).communicate()
        res_ping = str(ping_out).split("\\n")
        file_op = open("ping.log", "a")
        file_op.write(datetime + "\n")
        file_op.write("                     PING " + host +  "\n")
        #file_op.write(res_ping[1] + "\n")
        #file_op.write(res_ping[2] + "\n")
        #file_op.write(res_ping[3] + "\n")
        for i in range(len(res_ping)):
                file_op.write(res_ping[i] + "\n")
        file_op.write("########################### end ping #######################\n\n")

ping_func(lan_host)
ping_func(wan_host)
