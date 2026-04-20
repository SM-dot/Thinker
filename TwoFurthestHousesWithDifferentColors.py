# Leetcode 2078: Two Furthest Houses With Different Colors
# Problem Link: https://leetcode.com/problems/two-furthest-houses-with-different
# Category: Array, Two Pointers
# Difficulty: Easy

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        '''
        there could be many ways to solve this problem 

        1. Brute force, for each house color, go through every other color and calcualte the ditance between them. 
        2. Another approach could be:
        you know the edges are a house color anything in between will give u the longest distance so u fix the edges 
        you do this from the right and the left cause the largest distacne could be from both the sides. 
        This is O(n)
        O(n)
        so total time complexity is then O(2n)

        but it is possible that u are told to do it in O(n) single pass, 
        you simply run a loop from i = 0 to n and keep track of the largesgt difference beween houses from poistion 0 and position n - 1.

        Okie, now let's code! 
        '''
        n = len(colors)
        result = 0 

        i = 0
        while colors[i] == colors[n - 1]:
            i += 1
        
        result = max(result, abs(i - (n - 1)))

        i = n - 1
        while colors[i] == colors [0]:
            i -= 1
        
        result = max(result, i)

        return result 
        