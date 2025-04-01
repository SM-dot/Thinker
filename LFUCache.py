# Leetcode Link: https://leetcode.com/problems/lfu-cache/
# Category: Data Strcutures, Maps

'''
Ok we need multiple data structures here. 
1. To store the count/ frequency  - maybe a map 
2. To store the key,value pairs that exist in cache and lookup is O(1) - map certainly (seen in LRU cache question before)

Ok, now let's see the count frequency map in more detail 
Since we would need to remove the node which has been least frequently used we would need this data structure to be ORDERED. Then we can just refer to the counter which is at 0th position this frewuncy could be 1, 2, 3, anything based on the freq so ordering is important cannot just say counter_map[1], cause the least frequency can be 10 as other frequencies are 30, 40, etc...


Ok, now if there is a tie in the frequencies of nodes, which means that there can be multiple nodes or key value pairs with the same frewuency then we select the least recently used. This means that our counter map, key would be the frequency and value would be some sort of a list. 

Deeper dive into the list - the list needs to be a doubly linked list only then can we remove, insert, delete in O(1) time - this is intuitive because of the LRU cache question. 

Python specific: use ordered dict which will act as a dll 

Classes to create: 
Node 
This would have the value, frequency

Maps:
Cache - Key: key, Value: Node
Freq_map - Key: frequency, Value: Doubly Linked List/ ordered dict 

Let's code!
'''
class Node: 
    def __init__(self, val, count):
        self.val = val
        self.count = count

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodeKeys = {}
        self.nodeCounts = defaultdict(OrderedDict)
        self.minCount = None
        

    def get(self, key: int) -> int:
        if key not in self.nodeKeys:
            return -1
        
        node = self.nodeKeys[key]
        # remove from current bucket 
        del self.nodeCounts[node.count][key]
        # put in new bucket 
        node.count += 1
        self.nodeCounts[node.count][key] = node

        # update minimum count 
        if not self.nodeCounts[self.minCount]:
            self.minCount += 1
        
        return node.val


    def put(self, key: int, value: int) -> None:
        if not self.cap:
            return 
        
        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key)
            return 
        
        if len(self.nodeKeys) == self.cap:
            # remove items
            # return the node, only interested in key
            lfuKey, lfuCount = self.nodeCounts[self.minCount].popitem(last=False) # pops the head which was first added in the dictionary 
            del self.nodeKeys[lfuKey]
        
        newNode = Node(value, 1)
        self.nodeKeys[key] = newNode
        self.nodeCounts[1][key] = newNode
        self.minCount = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
