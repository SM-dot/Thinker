# LeetCode Problem Link: https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-right/
# LeetCode Problem: 2568. Maximum Number of Operations to Move Ones to the Right
# Category: Array

class Solution:
    def maxOperations(self, s: str) -> int:
        '''
        Ok so for this one it is important to know that we need to maximize. 
        If we go from right to left we would get the least operations, cause we have alreayd moved the ones to the side, so less operations would happen. 

        If we go from left to right, then more operations would happen cause 0's would come. 

        Also note what the question is asking:
        1. we need the MAX operations till all the 1's are on the right hand side 
        2. we can keep on moving 1 till 2 conditoins:
            1. we do not reach the end opf the array 
            2. we reach another 1
            both of these mean one operation has been done 
        
        Ok, so now if u observe, the number of operations for each moving 1 through 0's is the number of 1's u have before that 0. 

        For example, u have 
        10001101
        so for it to become 
        00011101 
        this is just 1 single operation


        So the story is: 
        1. count the number of 1's before a 0
        2. add it to the counter 
        3. move i to the next index of seeing 1-> cause remeber moving 10001 is just 1 opeation

        Now let's code! 
        This is also in O(n)
        and note that the most important 2 points in this story are that 
        we traverse left to right for max answer 
        and count the number of 1's before a 0
        Time complexity of this code is O(n)
        Space complexity of this code is O(1)
        cause u dont need anymore space
        This is a simple find pattern and trick problem
        '''
        n = len(s)
        numberOfOnes = 0
        countOperations = 0
        i = 0

        while i < n:
            if s[i] == '1':
                numberOfOnes += 1
                i += 1
            else:
                countOperations += numberOfOnes
                # cause we need to finish that operation for the ones that came before 
                while i < n and s[i] != '1':
                    i += 1
        
        return countOperations
