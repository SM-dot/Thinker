// Leetcode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
// Problem Number: 80
// Category: Arrays and fillIndex

class Solution { 
public:    
    // This solution efficiently removes duplicates from a sorted array, allowing at most two occurrences of each number.
    // The approach uses a single-pass strategy with two pointers: fillIndex tracks where to place the next valid number,
    // and i iterates through the array starting from the third element (index 2). Since the array is sorted and we allow
    // two duplicates, we can include a number if it's different from the number two positions back (fillIndex - 2).
    // This ensures we never exceed two copies of any number. The algorithm runs in O(n) time and O(1) space as it
    // modifies the array in-place, making it optimal for both time and space complexity.
    int removeDuplicates(vector<int>& nums) {        
        if (nums.size() <= 2)            
            return nums.size();        
        int fillIndex = 2;        
        int n = nums.size();        
        for(int i = 2; i < n; i++)        
        {            
            if (nums[fillIndex - 2] != nums[i])            
            {                
                nums[fillIndex++] = nums[i];            
            }        
        }        
        return fillIndex;    
    }
};
