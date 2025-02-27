// Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence/description/
// Problem Number: 128
// Category: Sets 

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        /*
        Firstly think of the question like this: we have a bag of numbers
        We can create sequences of numbers like this:
        1 2 3 4 
        78 79 80 81..
        based on what is inside the bag
        Now we have to find the longest consecutive elements subsequence
        If we pick out a number it can be in the middle of the sequence, end of the sequence or start of the sequence. 

        If I pick out a number from the bag it can be anything! 
        If it is in the middle of the sequence I will have to find all the elements less than that number, then all the elements greater than that number 
        -- too much work

        If I pick out a number that is the end of the sequence then I keep on going back ( if element + 1 number is not in the bag that means it is the end of the sequence)

        However, most intuitive method is to see if the number I got from my bag is the begining of the sequence or not. Check: if number - 1 does not exist in the bag this means that it is the begining of a fresh new sequence. 

        From here I run a loop and find all the numbers ahead in the sequence and note the length. 

        Bag can be a set so that look up is O(1)

        Time Complexity: We will check all the elements in nums to see if it is the starting of the sequence or not, if it is the starting we find the rest of the numbers but no number will we be accessing more than once thus the T.C is O(N) and space is also O(N) - for our bag or set
        */

        unordered_set<int> bag(nums.begin(), nums.end());
        int maxLength = 0;

        // edge case code
        if (nums.size() == 0)
            return maxLength;

        for(auto& num: nums)
        {
            // we have found the start of a sequence
            if (bag.find(num - 1) == bag.end())
            {
                int seqLength = 1;
                int currNum = num;
                while(bag.find(currNum + 1) != bag.end())
                {
                    seqLength += 1; 
                    currNum += 1;
                }
                maxLength = max(seqLength, maxLength);
            }
        }

        return maxLength; 
    }
};
