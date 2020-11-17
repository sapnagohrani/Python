from time import time
import sys
from threading import Thread

sys.setrecursionlimit(10 ** 6)
factorial_list = [3900, 3800, 3700, 3600, 3500] * 100


def get_factorial(num):
    if num == 1:
        return 1
    else:
        return num * get_factorial(num - 1)


class FactorialThreading(Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.factorial = 0

    def run(self):
        self.factorial = get_factorial(self.num)
        print(self.factorial)


s = time()
threads = []
for n in factorial_list:
    thread = FactorialThreading(n)
    thread.start()
    threads.append(thread)
# Wait for all threads to finish
for thread in threads:
    thread.join()
e = time()

print('total sec' + str(e - s))
