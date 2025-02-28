// Leetcode link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
// Problem Number: 27

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // [0,1,2,2,3,0,4,2]
        // [0,1,3,0,4]
        // I like to call this method the fill index method
        // Where I need to modify the array in place, a fill index helps keep track of where u can fill
        // for example, initially your fill index is 0, if val = 2
        // 0 can be filled, then 1, now your fill index is at position 2 and the value there is 2 but I do not want to put 2 in my nums so my fill index remains at index 2, then when I reach 3 whose original index is 4, i put it in fill index 2.
        // T.C: O(N) - iterating through all elements once
        // S.C: O(1) - taking no extra space 


        int fillIndex = 0;
        int n = nums.size();

        for(int i = 0; i < n; i++)
        {
            if (nums[i] != val)
            {
                nums[fillIndex] = nums[i];
                fillIndex += 1;
            }
        }

        return fillIndex;
    }
};
