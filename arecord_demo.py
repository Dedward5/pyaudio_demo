# sudo0 arecord -D plughw:1 --duration=10 -f cd  -vv test10.wav

import  subprocess, os, sys
import threading
import time

cmd1= "arecord -D plughw:1 -f cd -vv /media/usb/recorded7.wav"
pro1= subprocess.Popen("exec " + cmd1,stdout=subprocess.PIPE, shell=True)



print("Audio record is only for 10sec")

for i in range (25):
	time.sleep(1)
	print (i)

print("I quit")

pro1.kill()
#thread.stop()
