# Leetcode Link: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# Leetcode Name: Detect Patterns of Length M Repeated K or More Times
# Category: Array, Hashing, Sliding Window

class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        '''
        Ok, so the brute force approach what u thought was that that we keep track of the pattern and then keep a dictionary and add it in the dictioanry, whenever the count exceeds the k value we return True 
        However, a key difference that is there and needed is that the pattern is repeated consecutively not just once or twice. So that is the main thing here. 

        2 constraints that exist: 
        1. That the pattern must be continous 
        2. The pattern can start from any index 

        So we can start the pattern search from each index and then return when we hit k. This would have a time complexity of O(n square)

        Time Complexity: O(n^2) where n is the length of the array
        Space Complexity: O(1) as we are not using any extra space
        '''

        n = len(arr)

        for i in range(n - m + 1):
            pattern = arr[i: i + m]
            j = i
            count = 0
            while j <= (n - m):
                nextPattern = arr[j:j + m]
                if nextPattern == pattern: 
                    count += 1
                    if count >= k:
                        return True 
                else:
                    break
                j = j + m
        return False 





