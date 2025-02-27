// Leetcode Link: https://leetcode.com/problems/top-k-frequent-elements/
// Problem Number: 347
// Category: Maps and vectors

/*
Time Complexity: O(n) - We iterate through the input array to build the frequency map (O(n)), then iterate through the map to populate the frequency buckets (O(n)), 
and finally extract the top k elements in O(n), leading to an overall O(n) complexity.
Space Complexity: O(n) - We store frequency counts in an unordered_map (O(n)), use a frequency bucket array of size n+1 (O(n)), and store the result in a 
vector of size k (O(k)), which results in O(n) overall.
*/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map; // Stores the frequency of each unique number
        int n = nums.size();

        // Count the frequency of each element
        for(auto& num: nums) {
            map[num] += 1;
        }

        // Bucket array where index represents frequency and values store numbers with that frequency
        vector<vector<int>> freq_order(n + 1);

        // Populate the frequency buckets
        for(auto& p: map) {
            int element = p.first;
            int freq = p.second; 
            freq_order[freq].push_back(element);
        }

        int max_f = n; // Start checking from the highest possible frequency
        vector<int> answer;

        // Extract the top k frequent elements
        while(k > 0) {
            vector<int> vec = freq_order[max_f]; // Get elements with current frequency
            if (!vec.empty()) {
                for(int i = 0; i < vec.size(); i++) {
                    if (k > 0) {
                        answer.push_back(vec[i]);
                        k -= 1;
                    } else {
                        return answer;
                    }
                }
            }
            max_f -= 1; // Move to the next lower frequency
        }

        return answer;
    }
};
