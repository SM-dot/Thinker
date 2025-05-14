# Leetcode Link: https://leetcode.com/problems/partition-equal-subset-sum/description/
# Category: Recursion and DP 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        As you can see this problem is very similar to a knapsack porblem. How? 
        Knapsack problem: 
        Problem: which all items to put in our bag of size W such that the value or profit is maximised? 
        1. Have a camapcity or also populalrly known as the Weight/ W 
        2. Has a weights array 
        3. Has a values array 
        4. Trying to maximise the profit or values
        5. KEY: For each item we try and decide if we should put it in the bag or not.
        Similarly, for this problem let's find we will ask if we should have x number in the subset or not. This is the key idea, also populalrly known as the inclusion, exclusion principle. Since we can see the similarity with the knapsack problem we know that this can be solved with Dynamic Problem, particulalrly I will be solving it using tabulation or a top down approach. 

        Similarity with the knapsack problem: 
        weights array = nums 
        Ok, now let's see what our Weight or Sum is in this case. 
        We know sum of array, let's take an example 
        [1, 5, 11, 5] = 1 + 5 + 11 + 5 = 22
        which is an even number, thus if we have to split it into 2 equal parts it means that each part would have a sum of 11. If we find a subset of sum 11, naturally the remanining numbers will be summing to 11. 
        If the sum of the array is an odd number means that we cannot divide it into 2 equal arrays. 

        Now, we have the sum or the weight. We have our weights arrey which is nums. How do we initialize our DP? We know that the DP dimensions = [n + 1][sum + 1]
        if the number of elements is 0 and the sum we are aiming for is 0, then True in the grid. 
        If the number of elements is x and the sum is 0, then also True in all those places as an empty set will be considered as the answer. 
        If the number os elements is 0 (n = 0) and the sum is greater than 0, then there is no way we can make a sum without any values, thus here the grid will be filled with False. 

        Now, let's make our decision tree: 
        if nums[i - 1] > sum: 
            do not add it in the subset == t[n][sum] = t[n - 1][sum]
        if nums[i - 1] <= sum: 
            we can either include it in the subset or not include it
                        EXCLUDING, SUM IS UNCHANGED       INCLUDING HERE, SUM IS UPDATED 
            t[n][sum] =      t[n - 1][sum]            or     t[n - 1][sum - nums[n - 1]]
        
        The answer will be at t[n][sum] which will tell us if we can make a subset of sum 11, if yes then return True if not then False. 
        Now, let's code!

        NOTE: Taking sum as sum1 cause sum is a keyword in Python

        '''
        sum1  = 0
        n = len(nums)
        for num in nums: 
            sum1 += num
        
        if sum1 % 2 != 0:
            return False 
        
        sum1 = sum1 // 2
        t = [[False for j in range(sum1 + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            t[i][0] = True  # 0 sum is always achievable

        for j in range(1, sum1 + 1):
            t[0][j] = False  # Non-zero sum is not achievable with 0 elements
        
        for i in range(1, n + 1):
            for j in range(1, sum1 + 1):
                if nums[i - 1] <= j: 
                    t[i][j] = t[i-1][j] or t[i - 1][j - nums[i - 1]]
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][sum1] 
