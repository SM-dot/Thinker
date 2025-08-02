# Leetcode 1342. Number of Steps to Reduce a Number to Zero
# Problem Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Category: Bit Manipulation, Math

class Solution:
    def numberOfSteps(self, num: int) -> int:
        '''
        Any odd number ends with a 1 in binary.

        Subtracting 1 from a binary number flips the rightmost 1 to 0, and may flip some trailing 0s to 1s depending on what's after it. 

        Subtracting 1 removes the rightmost 1 and makes the number even — preparing it for a division.

        Dividing by 2 is the same as shifting the bits right by 1.

        14 = 1110 (binary)
        Step 1: even → divide → 111 = 7
        Step 2: odd → subtract → 110 = 6
        Step 3: even → divide → 11 = 3
        Step 4: odd → subtract → 10 = 2
        Step 5: even → divide → 1
        Step 6: odd → subtract → 0
        Total: 6 steps 

        num = 7 (111)
        3 ones → 3 subtracts
        3 bits → 2 divides
        → 5 steps

        Total steps = 1 operation for every 1-bit
         + 1 operation for every bit (except the highest one, since last divide ends the number)
        '''
        if num == 0:
            return 0
        return num.bit_count() + (num.bit_length()-1)