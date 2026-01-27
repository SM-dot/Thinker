# LeetCode Problem Link: https://leetcode.com/problems/sort-colors/
# LeetCode Problem: 75. Sort Colors
# Category: Array, Two Pointers, Sorting
# Difficulty: Medium


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        We can use counting sort here 
        explanation:
        To sort an array containing only the values 0, 1, and 2 (
        representing colors), we can use a counting sort approach. We first count the occurrences
        of each color using a hash map (or dictionary). Then, we overwrite the original array
        by iterating through the possible color values (0, 1, and 2)
        and filling in the array based on the counts stored in the hash map. This ensures that
        all 0s are placed first, followed by all 1s, and then all
        2s, effectively sorting the array in a single pass after counting.

        Time Complexity: O(n), where n is the number of elements in the array, as we need to iterate through the array twice (once for counting and once for overwriting).
        Space Complexity: O(1), since the hash map will always have a fixed size of 3 (for the three colors), which is considered constant space.
        """

        hm = defaultdict(int)
        for num in nums: 
            hm[num] += 1

        i = 0 
        for num in range(3):
            while hm[num] > 0:
                nums[i] = num
                i += 1
                hm[num] -= 1
        
        