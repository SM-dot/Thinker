# LeetCode Problem: 137. Single Number II
# Problem Link: https://leetcode.com/problems/single-number-ii/
# Category: Bit Manipulation, Math
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        ***** Checking if kth bit is 1 ******
        example: 
        k = 3
        initial mask = 00...000
        mask << k => shifting mask by k digits to the left gives 00...100

        00...101  your number
     &  00...100  mask
        ---------
        00...100  you get 1 means the 3rd bit is a 1
        
        ****** Setting the kth bit as 1 *******
        example
        k = 2
        initial mask = 00...000
        mask << k => shifting mask by k digits to the left gives 00...010

        00...001 your number
      | 00...010 mask
        --------
        00...011 001 is now 011!

        ***** SOLUTION THOUGHT PROCESS ******
        we know that integers have 32 bits 
bit Index: 31...210     
            0...010 = 2
            0...010 = 2
            0...011 = 3
            0...010 = 2

        answer = 0..000

        the 0th bit columns has 3 zeroes, 1 one
        count zeroes % 3 == 0
        count ones % 3 != 0 => implies 1 is the first bit of our answer
        so we set the first bit of our answer as 1

        the 1st bit column has 4 ones, 0 zeroes
        count zeroes % 3 == 0
        count ones % 3 != 0 => implies the 1st bit of our answer is 1 
        so we set the first bit of our answer as 1

        Time Complexity: O(32 * n) = O(n)
        Space: O(1)
        Now let's code!
        '''
        answer = 0

        for k in range(32):
            countOnes = 0
            countZeroes = 0
            mask = 1 << k
            for num in nums:
                if mask & num == 0: #checking if kth bit is 1 or 0
                    countZeroes += 1
                else:
                    countOnes += 1
            

            # for kth bit of answer, setting it
            if countOnes % 3 != 0:
                answer = answer | mask
       
        # Handle negative numbers (convert to 32-bit signed integer)
        '''
        In Python negative numbers are represented using 2's complement
        If the last bit, 31st bit is 1 means we have a negative number
        So we need to fix it as currently it is a very large decimal number
        We can fix it by subtracting 2^32
        In python 1 << 32 is equivalent of 2^32
        '''
        if answer & (1 << 31):
            answer -= 1 << 32
        
        return answer