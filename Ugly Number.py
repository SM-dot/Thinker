# Leetcode Problem: 263. Ugly Number
# Link: https://leetcode.com/problems/ugly-number/
# Difficulty: Easy

'''
Explanation:
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. To determine if a given number n is an ugly number, we can repeatedly divide n by 2, 3, and 5 as long as it is divisible by these numbers. If we can reduce n to 1 by this process, then n is an ugly number; otherwise, it is not.

Time Complexity: O(log n) in the worst case, where n is the input number. This is because we are dividing n by 2, 3, or 5 repeatedly until it becomes 1 or a number that is not divisible by these factors.
Space Complexity: O(1) since we are using a constant amount of space.
'''
class Solution:
    def isUgly(self, n: int) -> bool:
        while ( n > 1):
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return n == 1
        