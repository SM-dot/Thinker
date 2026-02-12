# LeertCode Problem Link: https://leetcode.com/problems/print-in-order/
# LeetCode Problem: 1114. Print in Order
# Category: Concurrency
# Difficulty: Easy


from threading import Lock
class Foo:
    def __init__(self):
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock2.acquire()  # This goes ahaead and locks the process, till it is not released it will not execute whatever is happening. 
        self.lock3.acquire() 



    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock2.release() # this lock is now released, so it will go ahead and execute whatever is needed and wanted in that block


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock2.acquire()
        printSecond()
        self.lock3.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.lock3.acquire()
        printThird()