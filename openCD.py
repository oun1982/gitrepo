# coding: UTF-8
import platform
import os
import ctypes

# windows
if platform.system() == 'Windows':
	# need 'u' before "", if you are using UTF-8. if not you don't need to put it.
	ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	#ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
	print("Windows worked\n")
# OSX
elif platform.system() == 'Darwin':
	os.system("drutil tray open")
	#os.system("drutil tray closed")
	print("Darwin worked\n")

# Linux
elif platform.system() == 'Linux':
	os.system("eject cdrom")
	#os.system("eject -t cdrom")
	print("Linux worked\n")

# NetBSD
# thank you to the man who adviced me how to eject on NetBSD
elif platform.system() == 'NetBSD':
	#you must be su
	os.system("eject cd")
	print("NetBSD worked\n")


#######################################################
# Operation under this comment has not been confirmed #
#######################################################

# FreeBSD
elif platform.system() == 'FreeBSD':
#you can use cdcontrol without typing su password. but do it on your own responsibility.
#visudo /usr/local/etc/sudoers
#username ALL=(ALL) NOPASSWD: /usr/sbin/cdcontrol
	os.system("sudo cdcontrol eject")
	#os.system("sudo cdcontrol close")
	print("FreeBSD worked\n")


else:
	print("OS Unsupported\n")
# if needed
#	print "UIIIIIIIN"