import threading,time

def square(x):
    for i in x:
        print(i*i)
        time.sleep(0.5)

def cube (x):
    for i in x:
        print(i*i*i)
        time.sleep(0.5)
lista=[2,3,4,5,6,7,8]


start=time.time()

thread1=threading.Thread(target=square, args=(lista,))
thread2=threading.Thread(target=cube, args=(lista,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()


print('the code ran for',time.time()-start)

