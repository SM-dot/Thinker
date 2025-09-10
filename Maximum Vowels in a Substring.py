# Leetcode Problem: 1456. Maximum Vowels in a Substring
# Leetcode Link: https://leetcode.com/problems/maximum-vowels-in-a-substring/
# Category: String, Sliding Window

'''
Explanation:
We can use a sliding window approach to solve this problem efficiently. The idea is to maintain a window of size k and count the number of vowels in that window. As we slide the window from
left to right, we update the count of vowels by adding the new character that enters the window and removing the character that exits the window. We keep track of the maximum count of vowels encountered during this process.

Time Complexity: O(n), where n is the length of the string s. We traverse the string once.
Space Complexity: O(1), as we are using a fixed amount of extra space.
'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = len(s)
        count = 0
        maxCount = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while j < n:
            if s[j] in vowels:
                count += 1

            if j - i + 1 == k:
                maxCount = max(maxCount, count)
                if s[i] in vowels:
                    count -= 1
                i += 1
            
            j += 1
        
        return maxCount

