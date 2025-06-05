# Leetcode Link: https://leetcode.com/problems/missing-number/
# Category: Bitwise 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0 
        n = len(nums)
        # basically a xor a = 0, a xor 0 = a, a xor b = some value 
        # first xor all the numbers in nums 
        # so u will have somehting like this 0 ^ 1 ^ 3 = xor_sum
        # then u xor_sum with all numbers in range 0 to n + 1, and all duplicate sets will be 0, u will only be left with the number that was missing in the xor_sum and 0 xor a = a, that's how u get the answer! 
        for num in nums: 
            xor ^= num
        
        for num in range(n + 1):
            xor ^= num
        
        return xor