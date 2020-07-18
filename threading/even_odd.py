import threading
import time
numEvens=0
class myThread(threading.Thread):
    stopFlag=0
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
    def run(self):
        print("\n Starting ",self.name)
        time.sleep(1)
        self.display()
        print("\n Exiting ",self.name)
    def display(self):
        global numEvens
        while self.stopFlag!=1:
            Lock.acquire()
            num=int(input("Enter the number: "))
            if num%2==0:
                numEvens+=1
            print("",self.name,numEvens)
            Lock.release()
            time.sleep(1)
    def stop(self):
        self.stopFlag=0
Lock=threading.Lock()
thread1=myThread("ONE")
thread2=myThread("TWO")
thread1.start()
thread2.start()
time.sleep(20)
thread1.stop()
thread2.stop()
print("\n EXITING MAIN THREAD")