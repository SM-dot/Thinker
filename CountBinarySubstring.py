# Leetcode Link: https://leetcode.com/problems/count-binary-substrings/
# Category: Basic Logic 
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        Main idea: 
        find the number of groups, and for each group how many 0's and 1's 
        "001100111"
        keeping count of consecutive 1's 
        grouping: "00", "11", "00", "111"
                    2    2.     2.    3

        now, to sount substring, ans += min(group[i], group[i + 1])
        cause 0011 -> has 2 subsets 01, 0011 = 2 susbets
        000111 -> has 3 subsets 01, 0011, 000111 = 3 subsets 
        if you have 00111 -> 01, 0011 = 2 subsets 

        '''

        count = 1
        groups = []
        n = len(s)

        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else: 
                groups.append(count)
                count = 1
        groups.append(count)

        answer = 0
        for i in range(0, len(groups) - 1):
            answer += min(groups[i], groups[i + 1])
        return answer 
