# Leetcode Name: Maximum 69 Number
# Leetcode Link: https://leetcode.com/problems/maximum-69-number/

# time complexity: O(N) where N is the number of digits in the number
# space complexity: O(N) where N is the number of digits in the number
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        n = len(num)

        for i in range(n):
            digit = num[i]
            if digit == "6":
                num[i] = "9"
                break
        
        return int("".join(num))


#time complexity: O(logN) where N is the number of digits in the number
#space complexity: O(1)
class Solution:
    def maximum69Number (self, num: int) -> int:
        # more optimal solution not O(N) ANYMORE this will be in logarithmic time. 
        place = 1
        numCopy = num
        best = 0
        while num: 
            if num % 10 == 6:
                best = place
            num = num // 10
            place *= 10
        
        return numCopy + (3 * best)
