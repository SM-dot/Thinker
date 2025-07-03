# LeetCode 739. Daily Temperatures
# Problem Link: https://leetcode.com/problems/daily-temperatures/
# Category: Stack, Monotonic Stack  


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        For this question we can take a monotonic stack appraoch.
        A monotonic stack is nothing but a stack storing values in a decreasing or increasing manner. Since here we need to find the maximum to the right of any value we will keep a decreasing stack.
        Why decreasing? 
        Cause the top of the stack will tell you the next largest value closest to the current value. This will help us identigy the number greater than the current number that is closest to it and this works cause we build our stack from the RIGHT. This is crucial cause it means that in the stack we will have values that are greater than the current value but the smallest when travelling from the right thus making sure it is the first one. 
        
        [73,74,75,71,69,72,76,73]
        0   1.  2. 3. 4. 5. 6. 7

        answer = [1, 1, 4, 2, 1, 1, 0, 0]

        decreasing stack:
        1 - 74
        2 - 75
        6 - 76

        Time Complexity: O(n)
        Space Complexity: O(n)

        NOTE: In our stack we store the index not the value for easy logic and clean coding 
        Now let's code!
        decreasing means - top has smallest, bottom has largest value
        '''
        stack = []
        n = len(temperatures)
        result = [0] * n

        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]: 
                stack.pop()
            
            if stack:
                result[i] = stack[-1]-i
            stack.append(i)
        
        return result 
            