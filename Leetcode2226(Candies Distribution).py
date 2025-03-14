# Leetcode Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14
# Problem number: 2226
# Category: Binary Search 

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''
        Ok, firstly let's understand this question in simpler terms. 
        We have candy jars and kids. 
        All candies given to a kid must be from the same jar, but different kids can have candies from different jars. The number of candies given to each kid should be the same. 

        Let's say we have [5, 8, 6] candies in each jar and 3 kids. We want to maximize the number of candies, so naturally I pick up 8. Can I give 8 candies to each kid? 
        [5-8 -> not poss, 8-8 -> candy given to 1 kid, 6-8 -> not possible]
        so only 1 kid out of 3 was able to get candy
        let's see if we can dstribut 7 to each kid
        [5-7 -> not poss, 8-7 -> 1 kid gets candy, 6-7 -> not poss]
        still only 1 kid gets candy, not the right answer
        let's see if we can do 6, only 2 kids will get not 3 so not possible.
        If I do 5 candies, all kids can get! 

        VIP - look at another example
        [5, 10, 3] k = 3
        let's say we tried 10, 9, 8, 7, 6, and could not distribute these candies among 3 children
        Now we decide to do 5
        [5-5 -> 1 kid gets candy, 10-5=5 5-5=0 -> 2 kids get, 3-5 -> 0 kid gets]
        so in total 3 kids get, and 5 is the correct answer

        Brute force approach:
        1. Find the maximum number of candies
        2. then keep on checking if those number of candies can be distributed 
        let's say max candies is 8 so u try 8, 7, 6, 5 ...1 till u find the answer 
        T.C: O(n*n) - too much time and compute! 

        Optimal Approach: 
        The main thing you would have noticed is that you are trying numbers from 1 to max_no range, instead of linearly try binary search to bring the time complexity down. 
        This is called binary search on asnwer. If an answer is possible, store it and keep on checking in right interval. If answer not possible check in left interval. (Look at code, will make more sense)
        Time complexity: 
        Binary Search: O(log(maxCandies))
        Finding if x candies can be given: O(n) n = size of array
        total T.C: o(n log(maxCandies))
        S.C: No extra space taken, O(1)! 
        Let's code!  
        '''

        maxCandies = max(candies)
        l = 1
        r = maxCandies
        answer = 0

        def canDistribute(numCandies, children):
            for i in range(len(candies)):
                children -= candies[i] // numCandies # eg 10 candies in jar at i, from this can I distribute 5(numCandies) if yes, how many times? (thus using divide)
                if (children <= 0):
                    return True
            return False

        while(l <= r):
            mid = int(l + (r - l)/2)
            if (canDistribute(mid, k)):
                answer = mid
                l = mid + 1
            else:
                r = mid - 1
        return answer
