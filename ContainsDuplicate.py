# Leetcode Problem: https://leetcode.com/problems/contains-duplicate/
# Category: Array, Hash Table
# Difficulty: Easy

# Explanation:
# To determine if an array contains any duplicates, we can use a set to keep track of the
# elements we have seen so far. As we iterate through the array, we check if the current
# element is already in the set. If it is, we have found a duplicate and can return True.
# If we finish iterating through the array without finding any duplicates, we return False.
# Time Complexity: O(n), where n is the number of elements in the array, as we may need to check each element once.
# Space Complexity: O(n) in the worst   case, where all elements are unique and we need to store them in the set.
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
Pro: Extremely concise.

Con: It always traverses the entire list. Your original loop has a "short-circuit"—it returns True the moment it finds the first duplicate, which is often much faster for large lists with early duplicates.
        '''
        seen = set()

        for num in nums:
            if num in seen: 
                return True
            seen.add(num)

        return False 