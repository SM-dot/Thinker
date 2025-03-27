# Leetcode Link: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
# Category: Arrays

class Solution:
    def reverse(self, arr, start, end):
        i = start
        j = end
        while (i < j):
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j -= 1
        

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Multiple ways to solve this but look at a pattern here 
        [1,2,3,4,5,6,7] - original 
        [4 3 2 1 7 6 5] - reversing till n - k elements and reversing n - k to n
        [5 6 7 2 3 3 4] - reversing entire array gives this result 
        The best way to come up with this solution is to carefullye examine the array and notice the pattern that appears
        T.C: O(N)
        S.C: O(1) - taking no extra place as reversing in place in the array :)
        """
        n = len(nums)
        k = k % n

        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n)


        
