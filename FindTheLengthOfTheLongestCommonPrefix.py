# LeetCode Problem Link: https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# LeetCode Problem: 2433. Find the Length of the Longest Common Prefix
# Category: Array, Hash Table, String, Trie
# Difficulty: Medium


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        There are multiple ways to solve this question. Was asked in HRT OA on CodeSignal. 

        1. What I did, which is a very bad brute force 
        Go over eqach element in array 1, then for that element go over all the elements in the second array. 
        Then call a function which find the common prefix 
        BAD BAD BAD CODE 

        2. Another approach could be to use a hashmap and store all the prefixes of all the elements in array 1, then go ahead and comnpute the prefixes of the elements in the second array and keep on adding till u find a match. Will code this up 

        3. The most optimal solution here uses tries. Usually Tries is the best approach to take for finding prefixes 

        time complexity: O(n*m) where n is the number of elements in the longer array and m is the average length of the numbers in the arrays. This is because we are iterating through each element in the longer array and for each element, we are checking its prefixes against the hashmap which takes O(m) time in the worst case.
        space complexity: O(n*m) in the worst case, where n is the number of
elements in the longer array and m is the average length of the numbers in the arrays. This is because we are storing all the prefixes of the elements in the longer array in the hashmap, and in the worst case, each element could have a unique prefix of length m.
        '''

        # this is the second brute force solution 
        hm = set()
        result = 0

        def getNumberLength(num):
            count = 0
            while num > 0:
                num = num // 10
                count += 1
            return count 


        # adding all the prefixes in a hashmap 
        for num in arr1: 
            while num > 0:
                hm.add(num)
                num = num // 10
        
        for num in arr2: 
            while num not in hm and num > 0:
                num = num // 10 
            
            if num > 0:
                result = max(result, getNumberLength(num))
        
        return result 



# Trie Implmentation Added: 
# Time and space complexity of this code is the most optimized 
# Tc: O(n*m) where n is the number of elements in the longer array and m is the average length of the numbers in the arrays. This is because we are inserting each element of the longer array into the trie, which takes O(m) time in the worst case, and then we are searching for each element of the shorter array in the trie, which also takes O(m) time in the worst case.
# Sc: O(n*m) in the worst case, where n is the number of elements
# in the longer array and m is the average length of the numbers in the arrays. This is because in the worst case, each element of the longer array could have a unique prefix of length m, leading to a trie with n*m nodes.
class TrieNode: 
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currRoot = self.root
        word = str(word)

        # kinda redundant here, not the best code written 
        for letter in word: 
            if letter in currRoot.children: 
                currRoot = currRoot.children[letter]
            else:
                currRoot.children[letter] = TrieNode()
                currRoot = currRoot.children[letter]
    
    def search(self, word):
        # this is not a regular search we only keep on adding till the prefix allows 
        # this function returns the length thatw e found common, otherwise it returns 0 if nothing is common
        currRoot = self.root 
        word = str(word)
        answer = 0

        for letter in word: 
            if letter in currRoot.children: 
                answer += 1 
                currRoot = currRoot.children[letter]
            else: 
                break 
        return answer 
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        '''
        Now trying the Trie Implmentation
        For a Trie implementation we need 2 things here: 
        1. Insertion 
        2. Search or finding the most common prefix/ we can also call this the search feature for consistency, this is just modifying the existing Trie implementation, slight modifications to that code can lead to the answer
        '''
        myTrie = Trie()
        result  = 0

        for num in arr1: 
            myTrie.insert(num)
        
        for num in arr2: 
            result = max(result, myTrie.search(num))
        
        return result 
