# Leetcode 1566. Detect Pattern of Length M Repeated K or More Times
# Problem Link: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# Category: Array

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        '''
        Let's try and solve it with constant space and O(n) time
        baiscally 
        i = 0
        j = i + m
        kepe on checking if arr[i] == arr[j]
        if yes, count += 1
        if not, reset count = 0 as pattern is broken

        when count == (k - 1)*m return True
        why? - cause we are basically checking if all the charcters in the whole pattern were found, since j is ahead by one entire pattern length => we have to worry about 1 pattern less matching cause as i was catching up it covered it.
        T.C: O(N) where N is the length of the array
        S.C: O(1) as we are not using any extra space
        Using a sliding window approach to detect the pattern
        '''
        count = 0
        n = len(arr)

        for i in range(0, n - m):
            j = i + m
            if arr[i] == arr[j]:
                count += 1
                if count == (k - 1) * m:
                    return True
            else:
                count = 0
        return False 