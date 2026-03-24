# LeetCode Problem Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
# LeetCode Problem: 1335. Minimum Difficulty of a Job Schedule
# Category: Array, Dynamic Programming

# Time comp-lexity: O(n^2 * d) where n is the number of jobs and d is the number of days. This is because we are filling a dp table of size n x d, and for each entry, we are iterating through the remaining jobs to find the maximum difficulty for that day, which takes O(n) time in the worst case.
# Space complexity: O(n * d) for the dp table, which stores the minimum difficulty of scheduling the remaining jobs starting from a certain index with a certain number of days left. In the
# worst case, we may need to store the results for all combinations of job indices and days, leading to O(n * d) space usage.

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # edge case: if number of jobs is less than days then not poss 
        n = len(jobDifficulty)
        if n < d:
            return -1 
        
        dp = [[-1 for _ in range(d + 1)] for _ in range(n + 1)]

        def solve(idx, d):
            # BASE CASE: 
            # if you have only one day left, you have to do all remaning jobs in that one day and find the max disffciculty of that day and return it

            if dp[idx][d] != -1:
                return dp[idx][d]

            if d == 1:
                maxD = jobDifficulty[idx]

                for i in range(idx, n):
                    maxD = max(maxD, jobDifficulty[i])
                dp[idx][d] = maxD 
                return maxD 
            
            # OTHER DAYS 
            maxD = jobDifficulty[idx]
            finalResult = float("inf")

            # Try one by one with all possibilities 
            # 
            # Take index = {idx} wala job in first day
            # Take index = {idx, idx + 1} wala job in first day 
            # Take index = {idx, idx + 1, idx + 2} wala job in first day 
            # ... and so on...
            # then find the most optimal one among all the results 

            for i in range(idx, n - d + 1):
                maxD = max(maxD, jobDifficulty[i])
                result = maxD + solve(i + 1, d - 1)

                finalResult = min(finalResult, result)
            
            dp[idx][d] = finalResult 
            return finalResult 
        
        return solve(0, d)
            


        