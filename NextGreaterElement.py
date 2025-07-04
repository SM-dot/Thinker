## LeetCode 496. Next Greater Element I
# Problem Link: https://leetcode.com/problems/next-greater-element-i/   
# Category: Stack, Monotonic Stack

class Solution:
    def rightGreater(self, nums2): 
        '''
        Input: array
        Output: array with values that represent the next closest greater element to the right, -1 else
        '''
        stack = [] #decreasing stack storing indexes
        n = len(nums2)
        result = [-1] * n

        for i in range(n - 1, -1, -1):
            while stack and nums2[stack[-1]] < nums2[i]:
                stack.pop()
            if stack:
                result[i] = nums2[stack[-1]]
            stack.append(i)
        return result 

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Input: nums1, nums2
        Operations:
        - Convert nums2 to map values to indexes to make it easier to find
        equivalent values from nums1
        - Find the largest element to the right for nums2 and store in a nums2
        resultant array
        - Iterate over nums1 and find the greates element from nums2result
        Output: a list of values greater than the equivalent value of nums1 found in nums2
        '''
        # storing nums2 in a map
        num2map = defaultdict(int)
        for i, num in enumerate(nums2):
            num2map[num] = i
        
        # finding the greatest number to the right of each element
        nums2result = self.rightGreater(nums2)
        print(nums2result)

        # filling our output array
        result = []
        for num in nums1:
            nums2equivalent = num2map[num] #returns the index in nums2
            result.append(nums2result[nums2equivalent])
        return result 
        
