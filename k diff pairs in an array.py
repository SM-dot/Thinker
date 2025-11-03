# Leetcode 532. K-diff Pairs in an Array
# Problem Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/
# Category: Array, Hash Table

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        Cases:

        1. k > 0: Find pairs where one is num and the other is num + k. To avoid duplicates, we can sort mentally: always look for the larger one.
        2. k = 0: Pairs of the same number, but only if it appears ≥2 times.
        3. k < 0: Impossible (absolute diff can't be negative), return 0.



        Very Very important to understand why we only look for num + k and not num - k => to avoid duplicates 
        To find unique pairs (a, b) where |a - b| = k, we need b = a + k or b = a - k. Checking only a + k for each number a in a frequency map ensures we count each pair exactly once, assuming a < b (i.e., b = a + k). This avoids double-counting, as checking a - k would find the same pair when processing b (where a = b - k). For k > 0, iterating over each a and checking if a + k exists captures all pairs efficiently.
        # T.C: O(N) where N is the number of elements in nums
        # S.C: O(N) for the frequency map
        Using a frequency map to count occurrences of each number and then checking for pairs based on the value of k
        '''
        data = Counter(nums)
        answer = 0
        if k == 0:
            for key, v in data.items():
                if v > 1:
                    answer += 1
        else: 
            for key,v in data.items():
                if k + key in data: 
                    answer += 1
        return answer 
