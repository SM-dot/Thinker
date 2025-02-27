// Leetcode link: https://leetcode.com/problems/valid-anagram/
// Problem Number: 242
class Solution {
public:
    bool isAnagram(string s, string t) {
        /*
        A good way would be to simple, without thinking about code - come up with a way to tell if 2 words are anagrams. A kid would probably count the letters in word1 and word2 and match them. 
        For example if 'a' came in word1 3 times does it come in word2 also 3 times. 
        Now let's think about the code, from a layman approach we can see that we need to calculate the frequency of letters for each word and need to match it. 
        Usually frequency of a letter means we need some sort of a mapping mechanism. Intuitively you could go to hashmaps. 
        Create a hashmap for word 1, create a hashmap for word 2 and compare the hashmaps. 
        We could also use simple vectors or arrays instead of hashmaps. Since we know that the input will always be in lower case this means that all letters of numbered 1 - 26 should fit in this range. 
        so each array index corresponds to a letter. for example if my letter is 'b' the n 'b' - 'a' => 97 - 96(ascii values) correspods to index 1. 
        We can also use a single array instead of creating 1 for each word. In this when we see a character in word1 we increase the count by +1 if we see the character in word2 we do -1
        In the end if everything is 0 in our array means that the frequencies matched and it is an anagram. 
        However the second last approach is a bit cleaner and simpler to understand for beginners thus I have coded that out. 
        Time complexity: let n be the avg length of word s and word t. Then since iterating through each character the T.C is O(n + n) = O(2n) = O(n) as we can drop constants
        Space complexity: for arr1 O(26) for arr2 O(26) = O(2 * 26) = O(52) = O(1)
        */
        vector<int> arr1(26, 0);
        vector<int> arr2(26, 0);

        for(auto& ch: s)
        {
            arr1[ch - 'a'] += 1;
        }

        for(auto& ch: t)
        {
            arr2[ch - 'a'] += 1;
        }

        return arr1 == arr2;
    }
};
