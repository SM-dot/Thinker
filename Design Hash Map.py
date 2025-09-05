# Leetcode Problem 706: Design Hash Map
# Problem Link: https://leetcode.com/problems/design-hashmap/
# Category: Design, Hash Table, Linked List

'''
Logic:
T.C: O(N) for each operation in the worst case (when all keys hash to the same index)
S.C: O(M + N) where M is the size of the hash map (1000) and N is the number of unique keys stored
Using separate chaining with linked lists to handle collisions in the hash map  

'''
class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hm = [Node() for _ in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        curr = self.hm[key%1000]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        curr = self.hm[key%1000]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.hm[key%1000]

        while curr and curr.next:
            if curr.next.key == key: 
                curr.next = curr.next.next
                return 
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)