// Leetcode Problem Link: https://leetcode.com/problems/construct-smallest-number-from-di-string/description/?envType=daily-question&envId=2025-02-18

// BRUTE FORCE 
class Solution {
public:
    bool matchesPattern(string& ans, string& pattern)
    {
        int n = pattern.length();
        for(int i = 0; i < n; i++)
        {
            if ((pattern[i] == 'I' && ans[i] > ans[i+1])|| (pattern[i] == 'D' && ans[i] < ans[i+1]))
                return false;
        }

        return true;
    }
    string smallestNumber(string pattern) {
        // BRUTE FORCE 
        // T.C: O(n+1)! -> STL T.C for  next_permutation 
        // T.C: O(n) -> fits the pattern or not 
        // Total T.C: O(n *(n + 1)!)
        

        int n = pattern.length();
        string ans = "";

        // creating the first possible smallest answer which is 1234.. depending on the length of the pattern
        for(int i = 1; i <= n + 1; i++)
        {
            ans.push_back(i + '0'); // converts a number to string so if i = 1, this will store '1', i = 2 then stores '2'
        }


        while(!matchesPattern(ans, pattern))
        {
            next_permutation(begin(ans), end(ans));
        }

        return ans;
    }
};

// OPTIMIZED SOLUTION
class Solution {
public:
    string smallestNumber(string pattern) {
        // Using a stack 
        // Why stack - good for rectifying mistakes when there are multiple D's together in the patters 
        // develope the answer such that increment count by 1, starting from 1. 
        // Visiting each character once - O(N)
        // Stack push and pop - (O(1) + O(1)) for (n + 1) elements 
        // Therefore T.C: O(2(n+1)) = O(2n + 2) = O(n)
        // Stack S.C: O(n+1)
        // Let's code

        int n = pattern.length();
        int count = 1;
        string ans = "";
        stack<char> st;

        for(int i = 0; i <= n; i++)
        {
            
            st.push(count + '0'); // convert number to character trick
            count += 1;

            if (i == n || pattern[i] == 'I')
            {
                while(!st.empty())
                {
                    ans += st.top();
                    st.pop();
                }
            }
        }

        return ans; 
    }
};
