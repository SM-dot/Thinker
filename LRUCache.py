# 146. LRU Cache
# Problem Link: https://leetcode.com/problems/lru-cache/
# Category: Design, Hash Table, Doubly Linked List  

'''
Explanation:
To implement an LRU (Least Recently Used) Cache, we can use a combination of a hash map and a doubly linked list. The hash map will store the keys and their corresponding nodes in the doubly linked list, allowing for O(1) access time. The doubly linked
list will maintain the order of usage, with the most recently used items at the front and the least recently used items at the back. When we access or add an item, we move it to the front of the list. If the cache exceeds its capacity, we remove the item at the back of the list (the least recently used item).
 This code can be made cleaner by using helper functions to add and remove nodes from the doubly linked list, but for clarity, I've kept the operations inline.
 Time Complexity: O(1) for both get and put operations
 Space Complexity: O(n) where n is the capacity of the cache    
'''
class Node:
    def __init__(self, key = 0, val = 0, next = None , prev = None):
        self.next = next
        self.prev = prev
        self.val = val 
        self.key = key 


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.track = {} # maps keys to node 
        self.capacity = capacity 
        # front has recently used val 
        # back has least recently used 
        

    def get(self, key: int) -> int:
        if key not in self.track: 
            return -1 
        
        # update position 
        node = self.track[key]
        prevCurr = node.prev
        nextCurr = node.next 
        prevCurr.next = nextCurr
        nextCurr.prev = prevCurr
        currFirst = self.head.next
        self.head.next = node 
        node.prev = self.head
        node.next = currFirst
        currFirst.prev = node
        # return value 
        return node.val 

        

    def put(self, key: int, value: int) -> None:
        if key in self.track:
            # update position to front of q 
            node = self.track[key]
            prevCurr = node.prev
            nextCurr = node.next 
            prevCurr.next = nextCurr
            nextCurr.prev = prevCurr
            currFirst = self.head.next
            self.head.next = node 
            node.prev = self.head
            node.next = currFirst
            currFirst.prev = node 
            node.val = value 
        
        else: 
            if self.capacity == 0:
                # removing the LRU 
                lastNode = self.tail.prev
                secondLast = lastNode.prev
                secondLast.next = self.tail 
                self.tail.prev = secondLast
                del self.track[lastNode.key]
                self.capacity += 1
            # creating new node
            self.capacity -= 1
            new_node = Node(key, value)
            # adding to the front of the deque 
            currFirst = self.head.next
            self.head.next = new_node
            new_node.prev = self.head
            new_node.next = currFirst
            currFirst.prev = new_node
            self.track[key] = new_node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Testing code: 
instance = LRUCache(3)
instance.put(1, 4)
instance.put(2, 3)
instance.put(3, 9)

print(instance.get(1))
print(instance.get(2))
print(instance.get(3))
instance.put(6, 2)
print(instance.get(1))
print(instance.get(6))
