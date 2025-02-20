// Leetcode Link: https://leetcode.com/problems/find-the-town-judge/
// Problem Number: 997
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        unordered_map<int, int> personPeopleTrustPerson; // Stores the number of people who trust a given person.
        unordered_map<int, int> personPeopleTrustedByThisPerson; // Stores the number of people a given person trusts.

        // Edge case: If there is only one person (n == 1), they are the judge by default.
        if (n == 1)
            return 1;
            
        // Iterate over the trust pairs to populate the maps
        for(auto& person: trust)
        {
            int p1 = person[0]; // The person who trusts
            int p2 = person[1]; // The person being trusted

            personPeopleTrustPerson[p2] += 1; // Increment count of people who trust p2
            personPeopleTrustedByThisPerson[p1] += 1; // Increment count of people trusted by p1
        }

        // Iterate over the map that tracks how many people trust a given person
        for(pair combo: personPeopleTrustPerson)
        {
            // A judge is trusted by everyone except themselves (n-1 people)
            // and does not trust anyone (should not appear in personPeopleTrustedByThisPerson)
            if (combo.second == n - 1 && personPeopleTrustedByThisPerson.find(combo.first) == personPeopleTrustedByThisPerson.end())
                return combo.first; // Return the judge if found
        }

        return -1; // Return -1 if no judge is found
    }
};
