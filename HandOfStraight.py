# Leetcode Problem: 846. Hand of Straights
# Leetcode Link: https://leetcode.com/problems/hand-of-straights/
from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        '''
        Ok, so it is evident that this is a hashmap problem, the main things to solve this is to make sure u have some order in the input. For example go for an ordered set in the input and iterate over the keys, stop iterating over something that has frequency of 0 

        First basic O(1) check would be to make sure that the size of the input is divisible by the group size

        This would have O(nlogn) time and O(n) space complexity 

        Can we do better? I do not think so


        Now, let's code! 
        '''

        freqMap = defaultdict(int)
        n = len(hand)

        if n % groupSize != 0:
            return False 


        for num in hand:
            freqMap[num] += 1
        
        InpfreqMap = sorted(freqMap)

        for num in InpfreqMap: 
            freq = freqMap[num]
            while freq:
                freq -= 1
                couldMake = False 
                for i in range(groupSize):
                    if freqMap[num + i]:
                        freqMap[num + i] -= 1
                    else: 
                        return False 
                    if i == groupSize - 1:
                        couldMake = True 
                
            
        return True 
