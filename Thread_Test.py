from threading import Thread
import time
__author__ = 'oun1982'
class Thread_Test(Thread):
    def __init__(self,threadID,name,counter):
        Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def printTime(self,threadName,delay,counter):
        while counter:
            time.sleep(delay)
            print("%s : %s"%(threadName,time.ctime(time.time())))
            print(time.strftime("%Y-%m-%d %H:%M:%S"))
            counter -=1
    def run(self):
        print("Start "+self.name)
        self.printTime(self.name,self.counter,5)
        print("Exiting "+self.name)


thread1 = Thread_Test(1,"Thread-1",1)
thread2 = Thread_Test(2,"Thread-2",2)

thread1.start()
thread2.start()

