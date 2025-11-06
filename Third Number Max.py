# LeetCode Problem 414: Third Maximum Number
# Leetcode link: https://leetcode.com/problems/third-maximum-number/

'''
Approach: 
1. Sort the input list 'nums'.
2. Initialize a result list with the first element of 'nums'.
3. Iterate through the sorted 'nums' starting from the second element.
4. For each element, check if it is different from the last element in the result list
    to ensure uniqueness. If it is different, append it to the result list.
5. After processing all elements, check the length of the result list:
   - If it contains fewer than three unique elements, return the maximum element (last element of result).
   - Otherwise, return the third maximum element (third last element of result).

Kind of stack concept used, as we want to know the top most element seen so far to avoid duplicates
Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for the result list
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        result = [nums[0]]
        n = len(nums)

        for i in range(1, n):
            if result[- 1] != nums[i]:
                result.append(nums[i])

        if len(result) < 3:
            return result[-1]
        return result[-3]