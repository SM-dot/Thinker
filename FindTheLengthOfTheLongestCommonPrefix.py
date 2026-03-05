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
