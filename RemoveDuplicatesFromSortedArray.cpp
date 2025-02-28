// Leetcode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
// Problem Number: 26
// Category: Arrays

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        // this also uses the fill index concept 
        /*
        have an index which will behavie like u are filling a new array but that index is pointing to the nums - so the changes are beign made in place.

        Check if in nums at index - 1 the value is the same as the current value, if not then fill it in the fill index and move to the next element. 

        T.C: O(N) - visiting each element atleast once
        S.C: O(1) -  taking no extra space
        */

        int fillIndex = 1;
        int n = nums.size();

        for(int i = 1; i < n; i++)
        {
            if (nums[fillIndex - 1] != nums[i])
            {
                nums[fillIndex] = nums[i];
                fillIndex += 1; 
            }
        }

        return fillIndex;
    }
};
