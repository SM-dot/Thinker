# LeetCode Problem: 15. 3Sum
# Problem Link: https://leetcode.com/problems/3sum/
# Category: Array, Two Pointers, Sorting
# Time Complexity: O(n^2)
# Space Complexity: O(1) for the output list, O(n) for sorting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique and handle duplicates
        n = len(nums)
        result = []
        
        # Iterate over each element as the first number of the triplet
        for i in range(n - 2):
            # Skip duplicates for nums[i] to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            # Use two pointers to find pairs that sum to -nums[i]
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # Found a valid triplet, add to result
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left and right pointers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1  # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum
        
        return result