// Leetcode Problem: https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20
// Promblem No: 1980

class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        // Get the size of the input vector (number of binary strings)
        // This solution is based on the diagonal flipping approach, which ensures that the generated binary string is different from every string in the given list.
        int n = nums.size();  
        
        // Initialize an empty string to store the result
        string result = "";  

        // Iterate through each index from 0 to n-1
        for (int i = 0; i < n; i++) {  
            // Get the ith character of the ith binary string
            char ch = nums[i][i];  
            
            // Flip the character ('0' becomes '1', '1' becomes '0') and append to result
            result += (ch == '0') ? '1' : '0';  
        }  

        // Return the resulting binary string
        return result;  
    }
};
