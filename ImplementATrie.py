# Leetcode Link: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150
# Category: Trees, Grapbs, Trie 

'''
Think of trie as a tree, where each node is a letter and that node tells you where you can go from there 

Trie can also be thought of as a graph as seen above. 

In order to insert, search, startswith to a Trie it is good to have a structure that we can call as node. Please note that while it is possible to code this question without another data strcuture of node and it performs better in leetcode, creating a node data structure makes your code more modular in nature, easier to read, modify and adapt. 

Now, let's code! 
'''
class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        if not self.search(word):
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            
            curr.endOfWord = True 
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False 
            curr = curr.children[ch]
        return curr.endOfWord 
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
