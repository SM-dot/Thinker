# Problem Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2025-03-11

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i = 0 
        j = 0
        map = {'a': 0, 'b': 0, 'c': 0}
        count = 0

        while (j < n):
            map[s[j]] += 1
            
            while(map['a'] > 0 and map['b'] > 0 and map['c'] > 0):
                count += n - j
                map[s[i]] -= 1
                i += 1
            
            j += 1
        
        return count
