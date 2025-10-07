# Leetcode Problem: 17. Letter Combinations of a Phone Number
# Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium
# Category: Backtracking, Recursion, String
from typing import List

'''
Explanation:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
    
number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Tree explanation:
        2(abc)      3(def)
       / |  \      / |  \
      a  b   c    d  e   f
     /|\ /|\ /|\ /|\ /|\ /|\
    4(g,h,i)   5(j,k,l)   6(m,n,o)
    /|\        /|\        /|\
   g h i      j k l      m n o  
    /|\        /|\        /|\
    7(p,q,r,s) 8(t,u,v)  9(w,x,y,z)
    /|\        /|\        /|\
    p q r s    t u v     w x y z
    /|\        /|\        /|\
    9(w,x,y,z) 9(w,x,y,z) 9(w,x
,y,z)
We can see that this is a backtracking problem where we need to explore all possible combinations of letters for the given digits. We can use a recursive function to build the combinations by appending letters
corresponding to each digit and backtracking when we reach the end of the digits.

However, since strings in Python are immutable, we will create a new string for each recursive call instead of modifying the existing string. This way, we avoid the need to backtrack by removing the last character.
Simple logic: 
1. Create a mapping of digits to their corresponding letters.
2. Define a recursive function that takes the current index in the digits string and the current combination of letters.
3. If the current index is equal to the length of the digits string, add the current combination to the result list.
4. Otherwise, iterate through the letters corresponding to the current digit, and for each letter, call the recursive function with the next index and the current combination plus the letter.
5. Finally, return the result list.

Note: we update index + 1, not i. Index iterates over the digits, i iterates over the letters corresponding to the current digit.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time complexity: 
        # at max each digit has 4 charcaters 
        # thus for each charcater to combine with another it depends on number of digits in the input thus the T.C is O(4**N)
        n = len(digits)

        if n == 0:
            return []
        
        mapping = {
            '2': "abc", 
            '3': "def",
            '4': "ghi", 
            '5': 'jkl',
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz'
        }

        result = []
        def solve(index, temp):
            if index >= n:
                result.append(temp)
                return 
            
            ch = digits[index]
            string = mapping[ch]

            for i in range(len(string)):
                # temp += a
                solve(index + 1, temp + string[i])
                # temp remove a that was added
                # this is a backtrakcing problem but becuase in python strings are immutable, each time we create a new string 

            
        
        solve(0, "")
        return result 