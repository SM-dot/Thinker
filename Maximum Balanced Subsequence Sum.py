# Leetcode: Maximum Balanced Subsequence Sum
# Problem Link: https://leetcode.com/problems/maximum-balanced-subsequence-sum/
# Category: Dynamic Programming, Recursion, Memoization, Binary Search, Ordered Map
from sortedcontainers import SortedDict
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        '''
        Firstly, this one is a variation of LIS and if you try to do recursion or memoisation it will have a TLE error. Cause bottom up and recursion both work in O(n square) time. And if we look at the contraints that would make our time complexity wayyyyy too much. 

        Thus while those 2 methods do solve test cases we cannot submit it because we get TLE. 

        Now the correct answer: 
        The first thing here: 
        We create a map with the following key value pair

        key = nums[i] - i
        value = sum of the longest sequence with that nums[i] - i


        just rearranmging the equation 
        nums[ij] - nums[ij-1] >= ij - ij-1
        nums[ij] -  i(j) >= nums[i(j-1)] i(j-1)

        Now, from LIS the difference here is that we need the max sum not max length. 

        if we have all the nums[i] - i stored, we would notice that we need the max sum subsequence from that but that would again take n square time. 

        So, we need to optimize further. 
        We are storing the max sum till nums[i] - i

        we then come to a j index and do nums[j] - j. In our map we then find the key which has a value just less than nums[j] - j, we then take that sum and add it with the value at nums[j] and update our map. 

        Another thing, if we have our map like this 
        3 -> 13
        4 -> 12
        5 -> calculating

        we now have option for 3, 4 and since we are looking to store max sum we want to chose 3. Thus we also update maps, any value greater than our key with a smaller sum we delete it. 

        Ok, now Python does not have ordered map or upper_bound we gotta figure this out on our own
        '''
        n = len(nums)
        mp = SortedDict()
        ans = float('-inf')

        if max(nums) < 0:
            return max(nums)


        for i in range(n):
            newKey = nums[i] - i
            # bisect_right returns index of first key > nums[i] - i
            idx = mp.bisect_right(newKey)
            # we look for the greater one, cause greater - 1, will give us the index of the value less than equal to our current key instead of getting one smaller elemtn cause nothing gives that 

            curr_ans  = nums[i]
            # this if condition is to see that if there is no smaller element than the one we find we simply add it and cannot find smaller. 
            if idx > 0:
                prev_val = mp.peekitem(idx - 1)[1]
                if prev_val > 0:
                    curr_ans += prev_val
            
            mp[newKey] = max(mp.get(newKey, -float('inf')), curr_ans)

            idx = mp.bisect_right(newKey)
            keys_to_remove = []
            while idx < len(mp) and mp.peekitem(idx)[1] <= curr_ans:
                keys_to_remove.append(mp.peekitem(idx)[0])
                idx += 1

            for k in keys_to_remove:
                del mp[k]

            ans = max(ans, curr_ans)

        return ans

               