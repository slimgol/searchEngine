import threading
import time

def print_cube(arr):
	for num in arr:
		print("F1")
		print(num*num*num)
		time.sleep(0.7)

def print_square(arr):
	for num in arr:
		print("F2")
		print(num**num)
		time.sleep(0.7)

def sayHi():
	for i in range(10000):
		print("Hello")
		time.sleep(0.7)


l1 = [i for i in range(100)]
l2 = [i for i in range(400)]

t1 = threading.Thread(target=print_square, args=(l1,))
t2 = threading.Thread(target=print_cube, args=(l2,))
t3 = threading.Thread(target=sayHi)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.sayHi()

