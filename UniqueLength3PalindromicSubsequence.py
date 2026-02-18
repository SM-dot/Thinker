# LeetCode Problem Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
# LeetCode Problem: 1930. Unique Length-3 Palindromic Subse


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        basically think 3 
        _ _ _ 
        this means the first and last characters need to be the same 
        in the middle u can put anything 
        since we need unique we need to get a set of characters between the two indexes. 
        note: subsequence means that it needs to be in the order in which it appears in the original array but does not need to be contiguous 

        you find the left most index of a character and the right, get the set of characters in the middle 

        Also for finding left most and right most, u need to store all the characters in a set initially.

        Now. let's code!

        # TIME COMPLEXITY: O(n) to find the left most and right most index for each character and to get the unique characters in the middle, since we are doing this for at max 26 characters, it is O(26n) which is O(n)
        # SPACE COMPLEXITY: O(1) since we are only storing a set of characters which can be at max 26 characters, thus it is O(26) which is O
        '''

        letters = set(s)
        n = len(s)
        count = 0

        for letter in letters: # at max runs 26 times, cause max letters is 26 
            left_most_index = -1
            right_most_index = -1 

            for i in range(n): # n 
                if s[i] == letter:
                    if left_most_index == -1:
                        left_most_index = i
                
                    right_most_index = i 
            
            unique_char = set()
            for i in range(left_most_index + 1, right_most_index): # n 
                unique_char.add(s[i])
            
            count += len(unique_char)

        # time complexity: O(n + n = 2n = n )
        
        return count 
