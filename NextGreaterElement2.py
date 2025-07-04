# LeetCode 503. Next Greater Element II
# Problem Link: https://leetcode.com/problems/next-greater-element-ii/
# Category: Stack, Monotonic Stack  

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        Input: integer array with repeating numbers, nums - circular
        Operations: 
        - find the greater element to the right and extend original array to have all numbers repeated twice
        - since extending the array size, use modulo to find original index, store original index in stack as well
        Output: integer array for each value in nums, gives the greater value if it exists
        -1 else
        T.C: O(N)
        S.C: O(N)
        '''
        print(nums)
        stack = []
        n = len(nums)
        result = [-1] * n

        for i in range((2 * n) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                result[i % n] = nums[stack[-1]]
            stack.append(i % n)
        
        return result

