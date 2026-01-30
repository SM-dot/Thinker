// Leetcode Link: https://leetcode.com/problems/word-ladder/
// Probelem Number: 127
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        /**
        The main idea is to transform the original word to the end word
        the starting word first needs to be transformed into a word of the wordlist
        this can be done by changing only one of the letters of the word. 
        hit 
        _it
        h_t
        hi_
        _ fill with a-z and check if it is a match or not

        hit -> hot 
        from here i can go to 
        hot -> dot or lot
        lets take dot 
        hit -> hot -> dot -> dog or log
        lets take dog 
        hit, 1-> hot, 2 -> dot, 3-> dog, 4-> cog, 5 == target
        levels = 5 

        so it is bfs if you do the tree strucutre
        q data structure <word, level>
        at each level you add the word it is a match to the target word
        as soon as it matches the target word, because shortest path return the level


        convert the wordlist to an unordered_set as finding if exists in data structure is O(1). 

        no need to create a visisted set instead just look if it is in set 
        if the word is no longer in the set means it has been visited already
        */

        unordered_set<string> set(wordList.begin(), wordList.end());
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        set.erase(beginWord);

        // T.C: O(N * length of word * 26)
        while(!q.empty())
        {
            auto element = q.front();
            string word = element.first;
            int level = element.second;
            q.pop();

            // check if transformed word in set or not, change each character with a - z and after changing make sure it is set back to original

            if (word == endWord)
                return level; 
            // TC: O(LENGTH OF WORD * 26)
            for(int i = 0; i < word.size(); i++)
            {
                char original = word[i];
                for(char ch = 'a'; ch <= 'z'; ch++)
                {
                    word[i] = ch;
                    if(set.find(word) != set.end())
                    {
                        q.push({word, level + 1});
                        set.erase(word);
                    }
                }

                word[i] = original;
            }
        }


        return 0;

    }
};
/*
Python Solution: 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append(beginWord)
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        
        if beginWord in wordList:
            wordList.remove(beginWord)
        
        sequence = 1
        while q:
            n = len(q)
            for i in range(n):
                element = q.popleft()
                if element == endWord:
                    return sequence 
                
                for index in range(len(element)):
                    for ch in range(ord('a'),ord('z') + 1):
                        mutation = element[:index] + chr(ch) + element[index+1:]
                        if mutation in wordList:
                            wordList.remove(mutation)
                            q.append(mutation)
            sequence += 1
        return 0

*/

// REV Jan 30th, 2026