import threading
import time
def Printer1(n):
	for i in range(0,n):
		print("Thread 1 printing ",i)
		time.sleep(1)

def Printer2(n):
	for n in range(n,0,-1):
		print("Thread 2 printing ",n)
		time.sleep(1)

t1=threading.Thread(target=Printer1,args=(10,))
t2=threading.Thread(target=Printer2,args=(10,))


t1.start()
t2.start()

t1.join()
t2.join()


print("End of the program!")
