# Leetcode Name: Largest Combination With Bitwise AND Greater Than Zero
# Leetcode Link: https://leetcode.com/problems/largest-combination-with-bitwise-and-g
# Time Complexity: O(n * 32) where n is the number of candidates and 32 is the number of bits in an integer
# Space Complexity: O(1) as we are not using any extra space

class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        '''
        Ok so basically we want to find the cimbination of all the numbers that when we do and on bits wer get a value greater than 1. 

        First, write the binary representation of all the numbers in binary 

        1  0001
        2. 0010
        3. 0011
        7  0111
        9. 1001

        the u see which colun or bit position has the maximum number of 1's cause that will give us the max number of numkbers we can group. 

        cause it bitwise OR all the numbers need to be 1 to result in a 1. 

        and any bit position which is 1 is going to create a number which is greater than 0 and that is our benchmark. 

        That is what we are looking for, so thats it. 

        Easy peezy lemon squeezy


        If you want to find if a aprticular bit position is 1 or not then all you have to do it do bit 1 left shift bit position and and thta wigth the number 


        so lets say ur bit position is 1, then if u left shift it, then u are checking for the second position, so u go 1 to 31 bits. 

        Now lets codeeee
        '''

        maxCount = 0

        for bitPos in range(32):
            bitCount = 0
            for number in candidates: 
                if number & 1 << bitPos != 0:
                    bitCount += 1
            maxCount = max(maxCount, bitCount)
        
        return maxCount
