# Leetcode Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Cetgory: Data Structures & Tries(Optional) this problem can also just be solved with a set 

class TrieNode: 
    def __init__(self):
        self.children = {}
        self.endOfWord = False 
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        '''
        This needs to have a recursive and iterative part
        Iteratve when no wild card 
        Recursive when wild card 

        if I encounter '.' basically explore all possible letters that exist 
        explore all paths from there
        if a path exists return true 
        if not, backtrack and move to the next possible answer 

        To avoid confusion think that the wild card will always be placed at the front 
        '''
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                letter = word[i] 
                if letter == '.':
                    for all_other_nodes in curr.children.values():
                        if dfs(i + 1, all_other_nodes):
                            return True
                    return False
                else:
                    if letter not in curr.children:
                        return False
                    curr = curr.children[letter]
            return curr.endOfWord
        return dfs(0, self.root)
        
