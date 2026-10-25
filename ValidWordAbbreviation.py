# Leetcode Name: Valid Word Abbreviation
# Leetcode Link: https://leetcode.com/problems/valid-word-abbreviation/
# Category: String, Two Pointers, Simulation

def valid_word_abbreviation(word: str, abbr: str) -> bool:
    # Write your solution here
    # time complexity: O(N) where N is the length of the abbreviation
    # space complexity: O(1) as we are not using any extra space
    wordLen = len(word)
    abbrLen = len(abbr)

    abbrPointer = 0
    wordPointer = 0 

    while abbrPointer < abbrLen: 
        ch = abbr[abbrPointer]
        if ch == "0":
            return False

        if ch.isdigit() == False:
            if wordPointer >= wordLen or ch != word[wordPointer]:
                return False
            wordPointer += 1
            abbrPointer += 1
        
        else: 
            # this means it is not 0 and we have a number, we need to get 
            # the full number like the number can be multiple digits
            skipNumber = 0

            while abbrPointer < abbrLen and abbr[abbrPointer ].isdigit() : 
                skipNumber = 10 * skipNumber + int(abbr[abbrPointer ])
                abbrPointer += 1
            
            wordPointer += skipNumber 
        
    
    return wordPointer == wordLen and abbrPointer == abbrLen