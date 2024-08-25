import threading
import time
from concurrent.futures import ThreadPoolExecutor

#time used
def func(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)
    return seconds
    


def main(func):
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

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,5)
        
        print(future1.result())
        print(future2.result())
        print(future3.result())
    
    
    


def poolingDemo2(func):
    with ThreadPoolExecutor() as executor:
        
        l = [1,2,3,4]
        results = executor.map(func,l)
        for result in results:
            print(result)

poolingDemo2(func)