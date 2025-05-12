# Leetcode Link: https://leetcode.com/problems/word-search-ii/
# Category: Trie and DFS 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        if not self.searchWord(word):
            curr = self.root
            for letter in word:
                if letter not in curr.children: 
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.endOfWord = True 
    
    def searchWord(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children: 
                return False
            curr = curr.children[letter]
        return curr.endOfWord

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n = len(board)
        m = len(board[0])
        MyTrie = Trie()

        result = set()


        for word in words: 
            MyTrie.addWord(word)
        
        TrieRootNode = MyTrie.root

        def dfs(r, c, word, node):
            if r not in range(n) or c not in range(m) or board[r][c] == "#" or board[r][c] not in node.children:
                return 
            
            temp = board[r][c]
            word += board[r][c]
            node = node.children[board[r][c]]
            board[r][c] = "#"
            if node.endOfWord:
                node.endOfWord = False
                result.add(word)
            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)
            board[r][c] = temp 
        
        for i in range(n):
            for j in range(m):
                if board[i][j] in TrieRootNode.children:
                    dfs(i, j, "", TrieRootNode)
        return list(result) 
        
