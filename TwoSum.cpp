// Leetcode Link: https://leetcode.com/problems/two-sum/submissions/1486588356/
// Category: HashMaps, Two Pointers

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /**
        1. Sort the array and have two pointer approach 
        Does not work here as they need indices 
        sort(nums.begin(), nums.end())
        int i = 0; 
        int j = n - 1; 
        
        while (i < j)
        {
            if (nums[i] + nums[j] < sum)
                i += 1;
            else if (nums[i] + nums[j] > sum)
                j -= 1;
            else
                return {i, j};
        }
        
        T.C: O(NlogN(sorting) + N) = O(NlogN)
        S.C: O(1)
        
        2. Hashing
        In a hashmap store all the numbers and their indices 
        then go over each element in nums 
        check if target - nums is in hashmap and target - nums index != nums index
        if yes return the indices
        
        T.C: O(N)
        */
        
        map<int, int> hm;
        int n = nums.size();
        
        for(int i = 0; i < n; i++)
        {
            hm[nums[i]] = i; 
        }
        
        
        for(int i = 0; i < n; i++)
        {
            int look = target - nums[i];
            if (hm.count(look) != 0 && hm[look] != i)
            {
                return {i, hm[look]};
            }
        }
        return {};
      
    }
};