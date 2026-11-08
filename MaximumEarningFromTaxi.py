# Leetcode Problem: 2008. Maximum Earnings From Taxi
# Leetcode Link: https://leetcode.com/problems/maximum-earnings-from-taxi/


class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        '''
        Simple, sort out the input 
        Then decide whether to tka ethe passenger or not and then get the max profit for it 

        So see all the sequences you can have for something like this, and then retunr the max profit. 

        So the decision tree for something like this would be take or dont take, if i dont take the dirst one can I take the second one and it depends on if my end time  is less than equal to start time of the next one 

        Exactly same as leetcode 1235 max job profit question. Ok, now lets code it up!
       
        Time Complexity: O(n log n) where n is the number of rides. This is because we are sorting the rides based on their start time, which takes O(n log n) time. After that, we are using binary search to find the next eligible passenger for each ride, which takes O(log n) time for each ride. Therefore, the overall time complexity is O(n log n).
        Space Complexity: O(n) for the dp array that stores the maximum earnings for each ride
        
        '''
        rides.sort(key=lambda x: (x[0], x[1]))


        def findPassenger(curr, endTime):
            right = len(rides) - 1
            result = float('inf')

            while curr <= right: 
                mid = curr + (right - curr) // 2

                if rides[mid][0] >= endTime: 
                    result = mid 
                    right = mid - 1 
                else: 
                    curr = mid + 1 
            
            return result 

        dp = [-1 for _ in range(len(rides) + 1)]
        def solve(i):
            if i >= len(rides):
                return 0 
            
            if dp[i] != -1:
                return dp[i]

            startTime = rides[i][0]
            endTime = rides[i][1]
            tip = rides[i][2]

            nextEligiblePassenger = findPassenger(i, endTime)
            takePassenger = endTime - startTime + tip + solve(nextEligiblePassenger)
            skipPassenger = solve(i + 1)

            dp[i] = max(takePassenger, skipPassenger)
            return dp[i]
        
        return solve(0)