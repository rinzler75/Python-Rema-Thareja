import threading
import time
class myThread(threading.Thread):
    def __init__(self, name,msg):
        threading.Thread.__init__(self)
        self.name=name
        self.msg=msg
        self.stopFlag=0
    def run(self):
        print("Starting "+self.name)
        self.display()
        #time.sleep(1)
        print("Exiting "+self.name)
    def display(self):
        while self.stopFlag!=3:
            Lock.acquire()
            print("[",self.msg,"]")
            Lock.release()
            time.sleep(1)
            self.stopFlag+=1
Lock=threading.Lock()
thread1=myThread("ONE","HELLO")
thread2=myThread("TWO","WORLD")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("EXITING MAIN THREAD")