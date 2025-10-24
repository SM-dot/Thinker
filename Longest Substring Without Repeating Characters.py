## LeetCode Problem: 3. Longest Substring Without Repeating Characters
# # Problem Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# # Category: Sliding Window, Hash Table

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.

        Approach:
        - Use the sliding window technique with two pointers (left and right).
        - Move the right pointer through the string, adding characters to a set.
        - If a duplicate character is found, move the left pointer forward until the duplicate is removed.
        - At each step, update the answer with the size of the current window (right - left + 1).
        
        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(min(n, m)), where m is the size of the character set (e.g., 26 for lowercase).
        """
        left = 0 
        n = len(s)
        bag = set()
        answer = 0
        
        for right in range(n):
            if s[right] in bag:
                while s[right] in bag:
                    bag.remove(s[left])
                    left += 1
                    
            bag.add(s[right])
            answer = max(answer, right - left + 1)
        return answer
# REV October 24th