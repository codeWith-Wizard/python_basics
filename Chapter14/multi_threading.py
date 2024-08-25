import threading
import time

#time used
def func(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)
    
    
func(2)
func(3)
func(1)

t1 = threading.Thread(target = func , arg = [4])
t2 = threading.Thread(target = func , arg = [2])
t3 = threading.Thread(target = func , arg = [1])


#starting the thread and moving it aside and going ahead
t1.start()
t3.start()
t2.start()

#waiting for thread to join'
t1.join()
t2.join()
t3.join()