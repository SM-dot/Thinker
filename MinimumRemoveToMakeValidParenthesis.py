# Leetcode Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
# Category: Stack and basic logic 
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Simple and basic approach: 
        Whenever you are dealing with valid parenthesis in any form think of a stack. 
        Ok, now with a stack you know that usually you put open parenthesis in the stack. But here we will be putting the index cause whichever index is left in the stack it is making an unbalanced string and we want to omit it when building our answer. 

        It is also possible that you only have )))). In that case push to a set. Let's code
        '''
        stack = []
        removingIndexes = set()

        # Making sure we have stack with invalid parenthesis indexes ready and set also has invalid parenthesis
        for i, num in enumerate(s): 
            if num == "(":
                stack.append(i)
            elif num == ")":
                if not stack: 
                    removingIndexes.add(i)
                else:
                    stack.pop()
        # Whatever is left in the stack is invalid so adding it to the set
        for index in stack: 
            removingIndexes.add(index)
        
        # building answer with whatver is not in invalid set
        answer = []
        for i, element in enumerate(s):
            if i not in removingIndexes:
                answer.append(element)
        
        # converting answer to string cause in Python each time it would create a new string so using a list for appending and eventually just converting it to a string :)
        return "".join(answer)
