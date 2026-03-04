# LeetCode Problem Link: https://leetcode.com/problems/text-justification/
# LeetCode Problem: 68. Text Justification
# Category: String, Greedy
# Difficulty: Hard


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        '''
        Relatively straightforward question. 
        Just do as it says. 
        Keep it simple and manage code. 
        You might think u need recursion or something but NO. 
        Was asked in Hudson River Trading OA on CodeSignal 
        Think like u collect what to put in bucket, then u seal the bucket and make the nexg bucket

        gaddhe = spaces between the words = number of words on a line - 1
        bloop beep. 2 words => 1 space

        time complexity: O(n) where n is the number of words in the input list. This is because we are iterating through the list of words once to construct the justified text.
        space complexity: O(n) for the result list that stores the justified lines of text.
        '''
        width = maxWidth
        n = len(words)
        result = []
        i = 0 

        def buildLine(i, j, eachGaddhaSpace, extraSpace):
            line = ""

            for k in range(i, j):
                line += words[k]
                if k == j - 1:
                    continue 
                line += " " * eachGaddhaSpace

                if extraSpace > 0:
                    line += " "
                    extraSpace -= 1

            while len(line) < width: 
                line += " "
            
            return line


        while i < n:
            lettersCount = len(words[i]) # it is given in the question that the first word always fits the width
            j = i + 1
            gaddhe = 0

            while j < n and len(words[j]) + lettersCount + 1 + gaddhe <= width:
                gaddhe += 1
                lettersCount += len(words[j])
                j += 1 
                
            
            remainingGaddhe = width - lettersCount
            eachGaddhaSpace = 0 if gaddhe == 0 else remainingGaddhe // gaddhe
            extraSpace = 0 if gaddhe == 0 else remainingGaddhe % gaddhe

            if j == n: 
                eachGaddhaSpace = 1
                extraSpace = 0 
            result.append(buildLine(i, j, eachGaddhaSpace, extraSpace))
            i = j 
        
        return result 
