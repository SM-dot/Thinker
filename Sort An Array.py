# LeetCode Problem Link: https://leetcode.com/problems/sort-an-array/
# LeetCode Problem: 912. Sort an Array
# Category: Array, Divide and Conquer, Sorting, Heap Data Structure
# Difficulty: Medium


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ''' 
        Multnple algorithms to do so, one that is usually missed is called counting sort which is based on the range of min and max numbers in the array you are given. 

        Time compleity = O(N + K)
        N = time to find min, max element, filling the hashmap

        1. find the min element in the array, find the max element in the array, this gives the range
        2. store the elements count in a map
        3. iterate over the range you found, if freq > 0, add that number in the resulting array that many times

        Now, let's code!
        '''


        minE = float('inf')
        maxE = float('-inf')
        hm = defaultdict(int)

        for num in nums:
            if num < minE:
                minE = num
            if num > maxE:
                maxE = num
            hm[num] += 1
        
        result = []
        for num in range(minE, maxE + 1):
            while hm[num] > 0:
                result.append(num)
                hm[num] -= 1
        
        return result