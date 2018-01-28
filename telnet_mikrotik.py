import getpass
import sys
import telnetlib

bot = telnetlib.Telnet("192.168.1.244", 23)
user = b'osdadmin'# user to login
password = b'internet@osd' #password to login
bot.read_until(b'Username:')
bot.write(user + b'\r\n')
bot.read_until(b'Password')
bot.write(password + b'\r\n')
#bot.write(('enable').encode('ascii'))
#bot.write(('OSD@R-SL5').encode('ascii'))
#bot.write(("\r\n").encode('ascii'))
bot.write(b'terminal length 0' + b'\r\n')
bot.write(b'sh ver | inc IOS | mem' + b'\r\n')
bot.write(b'sh ip int br' + b'\r\n')
bot.write(b'exit' + b'\r\n')
res = bot.read_all()
str_res = (str(res))
sp_res = (str_res.split('\\r\\n'))
#print(sp_res)
for i in sp_res:
    print(i)

#print(sp_res)
#print(sp_res[3])
#print(sp_res[4])



