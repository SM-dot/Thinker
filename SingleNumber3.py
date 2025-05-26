# Leetcode Link: https://leetcode.com/problems/single-number-iii/
# Category: Bit Manipulation 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        Basics: 
        a xor a = 0
        0 xor b = b
        Your aim is to create 2 groups such that the 2 elements that are different are in different groups and have common elements in them for example: 
        Group 1: 5, 1, 1
        Group 2: 3, 2, 2

        In order to do this, when creating a group, see that for 3 and 5 which bit is different. Based on that, make the groups. Now how do you find which bits are different? 
        First xor eveyrthing: 
        1 xor 1 xor 3 xor 5 xor 2 xor 2 = 3 xor 5 

        basic rules: 
        1 xor 1 = 0
        0 xor 0 = 0
        1 xor 0 = 1
        0 xor 1 = 1

        011
        101
        ---
        110

        now from this total xor, I know that the first but where it is 1 means that there was a difference in bits among 3 and 5 or whatever x and y numbers I have. So I want to know this position, I can get this by right shifting. 

        Now, to create the mask: 
        Mask is nothing but the number you will AND with to see whihc group it belongs. Let's say u have 001 and you are grouping based on the second bit, then this will be in group A and 010 in group B 
        001 and 010 = 0 -> Group A
        010 and 010 = 1 -> Group B 

        Ok, now let's code!
        '''

        xor = 0
        for num in nums: 
            xor ^= num
        
        # finding the position 
        position = 0
        while xor & 1 == 0:
            position += 1
            xor >>= 1
        
        # creating the mask: 
        mask = 1 << position

        xor_a = 0
        xor_b = 0
        for num in nums:
            # crucial, dont do num & mask == 1 cause mask can be 0b0001
            if num & mask:
                xor_a ^= num
            else:
                xor_b ^= num
        
        return [xor_a, xor_b] 
