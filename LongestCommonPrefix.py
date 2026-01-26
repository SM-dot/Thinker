# Leetcode Problem: https://leetcode.com/problems/longest-common-prefix/
# Category: Array, String
# Difficulty: Easy

# Explanation:
# To find the longest common prefix among an array of strings, we can first sort the array
# lexicographically. After sorting, the longest common prefix will be the common prefix
# between the first and the last strings in the sorted array. We can then compare these two
# strings character by character until we find a mismatch. The substring from the start to
# the point of mismatch will be our longest common prefix.
# Time Complexity: O(n log n) due to the sorting step, where n is the number of strings.
# Space Complexity: O(1) if we ignore the space used for sorting. sorting usuallu takes O(log n) space.



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # rememeber that after sorting the first word will be the smallest in length 
        # we will be sorting lexicogrpahically which means that they would be done based on character and then whichever one is smaller that would come first 
        # there is nothing to remeber, ur brain goes ok what is I find the common string from word 1 and word 2, then 2 and 3 .. so on till the last. The trick is that u only need to compare the first and the last since that is the shortest  - THINK 
        # ab, ace, acer => a is the answer 
        # u can get that answer by justs checking between ab and acer 


        strs.sort()
        word1 = strs[0] #this will be shorter in length
        word2 = strs[-1]
        result = ""

        if len(strs) < 2:
            return strs[0]

        for i in range(len(word1)):
            if word1[i] == word2[i]:
                result += word1[i]
            else:
                return result 
        return result 


# METHOD 2: O(N*M) thats better 
        # Vertical scanning 

        result = ""
        if len(strs) < 2:
            return strs[0]
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i == len(word) or strs[0][i] != word[i]:
                    return result 
            result += strs[0][i] 
        return result