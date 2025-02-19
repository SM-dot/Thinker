// Link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/submissions/1548793811/?envType=daily-question&envId=2025-02-19
// Problem Number: 1415
// BRUTE FORCE 
class Solution {
public:
    // uses backtracking 
    // main thing is build the resulting array lexicographically
    // put smallest letter first in the place holder
    // _ _ _
    // a _ _ -> a b _ -> a b a *backtrack* a b _ -> a b c *backtrack* abb not allowed 
    // now a c _ ...
    // then strings with b _ _ 
    // so on and so forth 


    // T.C: _ _ _ _ _ _
    //.     3 2 2 2 2 2 =  number of combinations strings generated lexicographically
    // O(3 * 2 ^(n - 1)) -> number of combinations generated = O(2^n)
    // pushing back in the result takes O(n) time
    // Therefore T.C: O(n * 2^n)
    // S.C: O(n * 2^n) = in result we will be storing 2^n string each of size n 

    void solve (string& curr, int n, vector<string>& result)
    {
        if (curr.length() == n)
        {
            result.push_back(curr);
            return;
        }

        for(char ch = 'a'; ch <= 'c'; ch++)
        {
            // as we cannot have strings that have same letter twice consecutively 
            if (!curr.empty() && curr.back() == ch)
                continue;
            // The DO, EXPLORE, UNDO template is a classic template that helps solve backtracking problems 
            // DO
            curr.push_back(ch);
            // EXPLORE
            solve(curr, n, result);
            // UNDO 
            curr.pop_back();
        }
    }
    string getHappyString(int n, int k) {
        vector<string> result; 
        string curr = ""; 
        solve(curr, n, result); 
        if ( k > result.size())
            return "";
        return result[k - 1];
    }
};

// OPTIMIZED
class Solution {
public:
    // uses backtracking 
    // main thing is build the resulting array lexicographically
    // put smallest letter first in the place holder
    // _ _ _
    // a _ _ -> a b _ -> a b a *backtrack* a b _ -> a b c *backtrack* abb not allowed 
    // now a c _ ...
    // then strings with b _ _ 
    // so on and so forth 


    // T.C: _ _ _ _ _ _
    //.     3 2 2 2 2 2 =  number of combinations strings generated lexicographically
    // O(3 * 2 ^(n - 1)) -> number of combinations generated = O(2^n)
    // pushing back in the result takes O(n) time
    // Therefore T.C: O(n * 2^n)
    // S.C: O(n * 2^n) = in result we will be storing 2^n string each of size n 


    // OPTIMIZATION
    // instead of storing all 2^n strings we keep a counter and store just when counter == k this was saving a lot of space 
    // S.C: O(n) system stack space 
    // T.C: same as before if need to take out the last string 
    void solve (string& curr, int n, int& counter, int& k, string& result)
    {
        if (curr.length() == n)
        {
            counter += 1;
            if (counter == k)
                result = curr; 
            return;
        }

        for(char ch = 'a'; ch <= 'c'; ch++)
        {
            // as we cannot have strings that have same letter twice consecutively 
            if (!curr.empty() && curr.back() == ch)
                continue;
            // The DO, EXPLORE, UNDO template is a classic template that helps solve backtracking problems 
            // DO
            curr.push_back(ch);
            // EXPLORE
            solve(curr, n, counter, k, result);
            // UNDO 
            curr.pop_back();
        }
    }
    string getHappyString(int n, int k) {
        string result = ""; 
        string curr = ""; 
        int counter = 0;
        solve(curr, n, counter, k, result); 
        return result;
    }
};


