# Leetcode Problem 76: Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Difficulty: Hard
# Category: Hash Table, Two Pointers, Sliding Window


'''Explanation:
How to approach this problem:
1. We will use the sliding window technique to find the minimum window substring.
2. We will maintain two pointers, i and j, to represent the current window in the string s.
3. We will also maintain a frequency map to keep track of the characters in the string t.
4. We will keep a variable requiredCount to track the number of characters we need to complete the substring that contains all characters of t.
5. We will expand the window by moving the j pointer and update the frequency map and requiredCount accordingly.
6. When we have a valid window (i.e., requiredCount is 0), we will try to contract the window by moving the i pointer and update the frequency map and requiredCount accordingly.
7. We will keep track of the minimum window length and its starting index.
Time Complexity: O(n + m) where n is the length of string s and m is the length of string t. We traverse both strings at most once.
Space Complexity: O(1) since the frequency map will have at most 52 entries (26 lowercase + 26 uppercase letters).
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Intuitively we know sliding window
        keep i and j pointers and keep frequency map 
        also keep a variable which keeps trakc of required characters in substring to complete all characters in t
        '''

        n = len(s)
        m = len(t)

        if (m > n):
            return ""
        
        i, j = 0, 0
        requiredCount = m
        fMap = defaultdict(int)
        substrStart = 0
        windowLength = float('inf')
        for ch in t:
            fMap[ch] += 1


        while j < n:
            ch = s[j]

            if fMap[ch] > 0:
                requiredCount -= 1
            
            fMap[ch] -= 1

            while (requiredCount == 0):
                currLength = j - i + 1
                if currLength < windowLength:
                    windowLength = currLength
                    substrStart = i
                fMap[s[i]] += 1
                if fMap[s[i]] > 0:
                    requiredCount += 1
                i += 1
            
            j += 1
        
        if windowLength == float('inf'):
            return ""
        
        return s[substrStart: substrStart + windowLength]

            