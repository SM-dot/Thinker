# Leetcode 948: Bag of Tokens
# Problem Link: https://leetcode.com/problems/bag-of-tokens/
# Category: Array, Greedy, Two Pointers
# difficulty: Medium


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        '''
        Usually asked in google intervoews, the coding is not hard but breaking down the requirement and figuring out what is needed is hard and crucial to solve this problem. 

        Basic greedy approach here, we are sorting the array for that. 

        2 main operations: 
        1. if power >= tokens[i]:
            score increases 
            power decreases
        
        2. if score > 1: 
            power increases 
            score decreases
        
        goal is to maximize the score in the end 

        Thus we should aim to increase the power by the max amount and when decreasing power that should be by the least amount. 

        Thus we sort it and use it, code is clean and simple. Just figuring this out takes time. 

        Time complexity is O(n)
        '''

        n = len(tokens)
        i = 0
        j = n - 1
        tokens = sorted(tokens)
        maxScore = 0
        score = 0


        while i <= j: 
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
                i += 1
                maxScore = max(maxScore, score)
            
            elif maxScore >= 1: 
                power += tokens[j]
                score -= 1
                j -= 1
            
            else:
                return maxScore 
        
        return maxScore 
