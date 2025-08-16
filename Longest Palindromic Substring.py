# Leetcode 5. Longest Palindromic Substring
# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
# Category: Dynamic Programming, String 

# Better Solution for Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Input: A string s
        Operations:
        - Use Dynamic Programming to find the longest palindromic substring
        - Create a DP table where t[i][j] is True if the substring s[i:j+1] is a palindrome
        - Iterate through all possible substrings and update the DP table
        - Keep track of the maximum length palindrome found and its starting index
        Output: The longest palindromic substring in s
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table
        Using Dynamic Programming to find the longest palindromic substring
        '''
        n = len(s)
        t = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        maxLen = 1
        startingPoint = 0

        # 1 length substrings are palindromic
        for i in range(n):
            t[i][i] = True

        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if (s[i] == s[j] and L == 2):
                    t[i][j] = True
                elif (s[i] == s[j] and t[i + 1][j -1]):
                    t[i][j] = True 
                
                if t[i][j]:
                    if maxLen < j - i + 1:
                        maxLen = j - i + 1
                        startingPoint = i
        
        return s[startingPoint: startingPoint + maxLen]


# Recursive Overhead Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Brute force - check if all substrings are palindrome or not, keep track of maxLen
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table + recursive stack space 
        Using a recursive approach to find the longest palindromic substring
        '''
        maxLen = 0
        startingPoint = 0
        n = len(s)
        t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def palindrome(i, j):
            if i >= j:
                return True 
            if t[i][j] != -1:
                return t[i][j]
            if s[i] == s[j]:
                t[i][j] =  palindrome(i + 1, j - 1)
                return t[i][j]
            t[i][j] = False 
            return t[i][j]
        
        for i in range(n):
            for j in range(i, n):
                if palindrome(i, j):
                    if maxLen < j - i + 1:
                        startingPoint = i
                        maxLen = j - i + 1
            

        return s[startingPoint: startingPoint + maxLen]