import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_1():
    with lock1:
        print("Thread 1 acquired lock 1")
        time.sleep(1)
        with lock2:
            print("Thread 1 acquired lock 2")

def thread_2():
    with lock2:
        print("Thread 2 acquired lock 2")
        time.sleep(1)
        with lock1:
            print("Thread 2 acquired lock 1")

t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Program finished")