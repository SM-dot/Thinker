# Leetcode 13917: Get No Zero Integers
# Problem Link: https://leetcode.com/problems/get-no-zero-integers/ 
# Category: Math, Array

class Solution:
    '''
    Input: An integer n
    Operations:
    - Check if n is even, if so return two equal halves 
    - Iterate through numbers from 1 to n-1
    - For each number, check if both the number and its complement (n - number)
        contain no zeroes
    Output: A list of two integers that sum up to n and contain no zeroes
    T.C: O(n * log n) in the worst case, where n is the
    number of digits in n
    S.C: O(1) as we are not using any extra space
    Using a brute force approach to find two integers that sum to n and have no zeroes
    '''
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasNoZero(num):
            # TC: O(logn)
            while (num > 0):
                digit = num % 10
                if digit == 0:
                    return False
                num = num // 10
            return True 
        
        # Entire TC: O(nlogn)
        if n % 2 == 0:
            if hasNoZero(n//2):
                return[n//2, n//2]
        #O(n)
        for i in range(1, n):
            if hasNoZero(i) and hasNoZero(n - i):
                return [i, n - i]
        
        return -1