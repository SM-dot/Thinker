# Leetcode Problem: 8. String to Integer (atoi)
# Link: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium

'''
Explanation:
The function myAtoi converts a string to a 32-bit signed integer (similar to C/C++'s atoi function). It handles leading whitespace, optional sign, and numerical digits, while
also managing overflow and invalid input cases.
Time Complexity: O(n) where n is the length of the string. This is because we may need to traverse the entire string in the worst case.
Space Complexity: O(1) since we are using a constant amount of space.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = 0
        sign = 1
        i = 0
        
        if len(s) == 0:
            return 0 
        
        # for -- would be invalid so that also gets handled here 
        if s[i] in {'+', "-"}:
            if s[i] == "-":
                sign = -1 
            i += 1
        
        while  i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            
            # This is given in the problem, if the integer number exceeds the 32-bit signed integer range, then we modify it based on the instructions
            if num * sign > 2**31 - 1:
                return 2**31 - 1
            if num * sign < -2**31:
                return -2**31
        
        return num * sign
