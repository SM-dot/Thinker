// Leetcode: Paid, free access on Neetcode.io, link - https://neetcode.io/problems/string-encode-and-decode
// category: strings 

/*
This program is open to interpretation. This is good for understanding string manipulation and there can be 148721t34832... many solutions. 
My approach: 
#LENGTH OF WORD# 
as the string can have special characters and numbers this unique identifier becomes pretty handy in identifying the words. YOU CAN COME UP WITH YOUR OWN UNIQUE SOLUTION!! :)))))
Time Complexity: encoding - O(n), decoding -O(n)
This problem is good for revising strings in a creative manner. 
*/
class Solution {
public:

    string encode(vector<string>& strs) {
        string answer = "";
        for(auto& word: strs)
        {
            int n = word.size();
            answer += "#" + to_string(n) + "#" + word;
        }

        return answer; 
    }

    vector<string> decode(string s) {
        int n = s.size();
        int i = 0;
        vector<string> decoded; 
        while(i < n)
        {
            if (s[i] == '#')
            {
                string len = "";
                i += 1;
                while (s[i] != '#')
                {
                    len += s[i];
                    i += 1;
                }
                int length = stoi(len);
                i += 1;
                decoded.push_back(s.substr(i, length));
                i = i + length; 
            }
        }
        // #4#neet
        return decoded; 
    }
};
