#i guess this example has been old as most of people use threading class for multithreading in python
import thread
import time
def display_time(threadname,delay):
    count=0
    while count<5:
        time.sleep(delay)
        count+=1
        print("%s:%s"%(threadname,time.ctime(time.time())))
try:
    thread.start_new_thread(display_time,("ONE",100))
    thread.start_new_thread(display_time,("TWO",200))
except:
    print("Error: unable to start thread")