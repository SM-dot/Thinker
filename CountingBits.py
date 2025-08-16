# Leetcode link: https://leetcode.com/problems/counting-bits/
# Category: Bit Manipulation
# Option 1:  Cleaner code:
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        0 0000
        1 0001
        2 0010
        3 0011
        4 0100 = 1 + dp[0] = 1 + dp[i - 4] = 1 + dp[0] = 1 + 0 = 1
        5 0101 = 1 + dp[1] = 1 + dp[i - 4] = 1 + dp[1] = 1 + 1 = 2
        6 0110
        7 0111
        8 1000 = 1 + dp[0] = 1 + dp[i - 8] = 1 + dp[0] = 1 + 0 = 1
        How do u know dp[i-what?]
        that is called the offset
        the offset is set after 0, after 4, after 8 as u see
        so if offset * 2 == i
        mean we are starting a new block
        '''
        offset = 1
        dp = [0] * (n + 1) # the dp array acts as the answer 

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i # setting it to 1, 2, 4, 8, 16, 32...
            dp[i] = 1 + dp[i - offset]
        return dp
    
# Option 2: More explantory but lengthy code 
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        5 // 2 -> 1 101
        2 // 2 -> 0
        1 // 2 -> 1 
        total 1's = 2



        4 // 2 -> 0 100 
        2 // 2 -> 0 
        1 // 2 -> 1 
        total 1's = 1

        3 // 2 -> 1 011
        1 // 2 -> 1
        total 1's = 2

        2 // 2 -> 0 010
        1 // 2 -> 1 001
        '''
        def numOfBits(num):
            count = 0
            while num != 0: 
                bit = num % 2
                num = num // 2
                count += bit 
            return count
        answer = []

        for num in range(n + 1):
            answer.append(numOfBits(num))
        return answer 
