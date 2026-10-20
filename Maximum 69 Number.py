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
