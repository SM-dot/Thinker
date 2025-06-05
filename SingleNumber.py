# Leetcode link: https://leetcode.com/problems/single-number/
# Category: Bit Manipulation
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        a xor a = 0
        a xor b = some value 
        a xor 0 = a

        Using this logic we can see that all duplicate numbers will cancel out to 0 and the non dumplicate number let's say a xor 0 = a will give the answer! :)
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        xor = 0
        for num in nums: 
            xor ^= num
        return xor 