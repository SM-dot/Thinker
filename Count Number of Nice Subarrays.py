# Leetcode 1248: Count Number of Nice Subarrays
# Problem Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
# Category: Array, Hash Map, Prefix Sum



class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        '''
        Main idea: 
        find a subarray with k odd numbers, then go ahead and move it by one


        Multiple ways to solve this, very similar to number of subarrays with sum k.

        Basically in a map store the number of subarrays with k odd numbers, count as you go, then go ahead and subtract so curr sum - k if in map then add that to the result.
        Time complexity: O(n) where n is the length of the input array nums. This is because we are iterating through the array once to count the number of odd numbers and update the hashmap, and each operation on the hashmap (insertion and lookup) takes O(1) time on average.
        Space complexity: O(n) in the worst case, if all numbers in the input array
        '''
        mp = defaultdict(int)
        # key = subarrays with k odd numebers, value = count of those subarrays

        mp[0] = 1 # cause empty subarray has 0 odd numbers 
        odd = 0
        result = 0
        for num in nums: 
            if num % 2 != 0:
                odd += 1
            
            if odd - k in mp: 
                result += mp[odd - k]
            
            mp[odd] += 1
        
        return result 
            