import threading
import time
class myThread(threading.Thread):
    def __init__(self,name,count):
        threading.Thread.__init__(self)
        self.name=name
        self.count=count
    def run(self):
        print("Starting "+self.name)
        i=0
        while i<self.count:
            display(self.name,i)
            time.sleep(1)
            i+=1
        print("Exiting "+self.name)
def display(threadname,i):
    print(" ",threadname,i)
thread1=myThread("ONE",5)
thread2=myThread("TWO",5)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting main thread")