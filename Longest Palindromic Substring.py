# Leetcode 5. Longest Palindromic Substring
# Problem Link: https://leetcode.com/problems/longest-palindromic-substring/
# Category: Dynamic Programming, String 

# Better Solution for Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Input: A string s
        Operations:
        - Use Dynamic Programming to find the longest palindromic substring
        - Create a DP table where t[i][j] is True if the substring s[i:j+1] is a palindrome
        - Iterate through all possible substrings and update the DP table
        - Keep track of the maximum length palindrome found and its starting index
        Output: The longest palindromic substring in s
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table
        Using Dynamic Programming to find the longest palindromic substring
        '''
        n = len(s)
        t = [[False for _ in range(n + 1)] for _ in range(n + 1)]
        maxLen = 1
        startingPoint = 0

        # 1 length substrings are palindromic
        for i in range(n):
            t[i][i] = True

        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                if (s[i] == s[j] and L == 2):
                    t[i][j] = True
                elif (s[i] == s[j] and t[i + 1][j -1]):
                    t[i][j] = True 
                
                if t[i][j]:
                    if maxLen < j - i + 1:
                        maxLen = j - i + 1
                        startingPoint = i
        
        return s[startingPoint: startingPoint + maxLen]


# Recursive Overhead Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Brute force - check if all substrings are palindrome or not, keep track of maxLen
        T.C: O(N^2) where N is the length of the string s
        S.C: O(N^2) for the DP table + recursive stack space 
        Using a recursive approach to find the longest palindromic substring
        '''
        maxLen = 0
        startingPoint = 0
        n = len(s)
        t = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        def palindrome(i, j):
            if i >= j:
                return True 
            if t[i][j] != -1:
                return t[i][j]
            if s[i] == s[j]:
                t[i][j] =  palindrome(i + 1, j - 1)
                return t[i][j]
            t[i][j] = False 
            return t[i][j]
        
        for i in range(n):
            for j in range(i, n):
                if palindrome(i, j):
                    if maxLen < j - i + 1:
                        startingPoint = i
                        maxLen = j - i + 1
            

        return s[startingPoint: startingPoint + maxLen]
    

# Manacher's Algorithm (Optimal O(N) Solution)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Manachers Algorithm: 
        Basically uses the property of a palindrome that it is the mirror on both sides. 
        Time Complexity: O(N)
        Space Complexity: O(N)
        
        STEP 1:
        you have an array that keeps track of the length of the longest palindrome
        add # between each character. Why?
        MOM -> centered at O
        ABBA -> centre of palindrome is BB
        A#B#B#A -> centre is not the #
        M#0#M -> centre is O
        This basically takes care of palindromes of even and odd length


        STEP 2: 
        initially, centre = 0, right most boundary of longets palindrom found = 0 
        a.k.a centre = 0, right = 0
        now iterate through each character
        if our current character is inside the boundary of a palindrome we had found, then we can simply copy the mirror value. here we select the minimum of mirror value and right - i, cause we do not know beyond the right boundary 

      
        if we are not inside a palidnrome, we exapand and find the palindrome

        At last we check if we found a longer palindrome, that means our right boundary stretches and we update it. 
        '''
        s = "^#" + "#".join(s) + "#$"
    
        P = [0] * len(s)      # P[i] = radius of palindrome centered at i
        center = 0            # Center of the rightmost palindrome
        right = 0             # Right boundary of the rightmost palindrome
        
        # Step 2: Fill P array
        for i in range(1, len(s) - 1):
            # If inside current right boundary, use mirror to skip work
            if i < right:
                mirror = 2 * center - i
                P[i] = min(right - i, P[mirror])
            
            # Expand around center i
            while s[i + P[i] + 1] == s[i - P[i] - 1]:
                P[i] += 1
            
            # Update the rightmost boundary if we expanded further
            if i + P[i] > right:
                center = i
                right = i + P[i]
        
        max_len = max(P)
        center_idx = P.index(max_len)
        
        # Extract and clean the palindrome
        start = center_idx - max_len
        end = center_idx + max_len + 1
        return s[start:end].replace("#", "")
    

    class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Palindromic substring bottom up approach: 
        1. for a single length string yes it is a palindrome
        2. for a double length string it is paldindrome if s[i] == s[j]
        3. for all other string lengths > 2
            it is a palindrome if s[i] == s[j] and the middle of the string is also a palindrome 
            so essentially s[i + 1:j] is a palindrome 
        
        ok, also you are going to find all the palindromic lenghts, so u starts for lengths 1, 2, 3, and for each of these lengths u start at index i. so from index 1 a string of length 2, from index 2 a string of length 2 etc. 
        and the length u can check till is gonna be i + L - 1 this is also ur J 
        '''
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        count = 0

        for L in range(1, n + 1):
            for i in range(0, n - L + 1):
                j = i + L - 1 
                if i == j:
                    dp[i][j] = True 
                
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][ j - 1]
                
                if dp[i][j] == True:
                    count += 1
        return count 
                
                