'''
2    Brute Force:
3    create a list of some size n and add elements to it using hashing
4
5    Hashing = function which gives the key or which bucket to put th value in 
6
7    Now the issue with brute force even though it works is that athere can be collisions. To avoid collisions there are two methods we can use to solve: 
8    1. Chaining (this means creating lists for each bucket)
9    2. Open adressing (this means storing the value in the bucket next to it, however the issue here is that when u remove then what happens, 12 x 13 all of them are supposed to be stored in bucket 1 if we go to search for 13 in bucket one cause that x value happened we wont be able to find it) T
10
11    Common method is to use chaining. 
12    Issues with chaining: 
13    exceeding the load factor
14
15    load factor = number of elements inserted in the set / total number of buckets 
16    ideal load factor used in java is 0.75
17    If we exceed the load factor then we rehash which means that we increase the number of buckets by 2. But for simplicity for this question we will not be rehashing. Ok now let's code!!! 
18'''

class Node:
    def __init__(self, key=-1):
        self.key = key
        self.next = None

class MyHashSet:

    def getBucketNumber(self, k):
        return k % 10**4

    def __init__(self):
        self.mySet = [Node() for _ in range(10**4)]
        

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            bucketNumber = self.getBucketNumber(key)
            currPointer = self.mySet[bucketNumber]

            while currPointer.next: 
                currPointer = currPointer.next
            
            currPointer.next = Node(key)


        

    def remove(self, key: int) -> None:
        if self.contains(key) == True:
            bucketNumber = self.getBucketNumber(key)
            currPointer = self.mySet[bucketNumber]

            while currPointer.next: 
                if currPointer.next.key == key: 
                    currPointer.next = currPointer.next.next
                    return
                currPointer = currPointer.next


    def contains(self, key: int) -> bool:
        bucketNumber = self.getBucketNumber(key)
        currPointer = self.mySet[bucketNumber]

        while currPointer: 
            if currPointer.key == key: 
                return True 
            currPointer = currPointer.next
        
        return False 

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)