# LeetCode Problem Link: https://leetcode.com/problems/verifying-an-alien-dictionary/
# LeetCode Problem: 953. Verifying an Alien Dictionary
# Category: Hash Map, String, Simulation
# Difficulty: Easy


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        Good practice to do before Alien Dictionary. Main Algorithm: 
        1. Store the order of the alien dicrionary in a hash map such that the key is the character and the value is the index, this will tell us what comes before or after it. 

        2. compare adjacent words, start by comparing each character in the adjacent words (do this till the length of the first adjacent word, if the second word ends before the first one means there is an issue cause lexicogrpahically is also based on size). 

        3. When u meet the first differing character check if it is before/ in correct order/ less value in hashmap. If yes break, u are in correct order and do not need to check further 

        4. If incoorect order, return false

        Note in step 3 we are breaking, not returning. In the end if eveyrthing goes smoothly then return True

        T.C & S.C = O(N)
        Easy peasy lemon squeezy
        Ref Video: Neetcode, super neet short video
        '''


        orderList = {c:i for i, c in enumerate(order)} # basically maps character to index

        n = len(words)
        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w1[j] != w2[j]:
                    if orderList[w1[j]] > orderList[w2[j]]:
                        return False
                    break #cause we dont need to check entire hello and leetcode, to know if they are in correct order we just need to check h and l 
        return True 