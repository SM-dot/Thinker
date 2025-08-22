# Leetcode 721. Accounts Merge
# https://leetcode.com/problems/accounts-merge/
# Category: DSU 

class DSU: 
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)
        if x_parent == y_parent:
            return 
        
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parents[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parents[x_parent] = y_parent
        else:
            self.parents[x_parent] = y_parent
            self.rank[y_parent] += 1
    

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        1. Join all the accounts which have similar emails 
        let's say we are checking the account at index 1 which is "John" and in this the email we notice that emailxyz is already in account 0 (hashmap) then we know that account 0 and account 1 must be joined together 

        2. Now we find al the parents and children groups 
        We iterate over all the values of our previous map which are the parents/ leaders. then we group the emails

        3. In the end we format, so change index 1 account to account[1][0] which would have the name and also sort the list of emails

        DSU time complexity is O(amortised 1) here we are using path compression and optimising by rank. 
        If we consider total number of emails to be m, then the time complexity is O(mlogm) logm - sorting 
        Let's code!
        '''
        n = len(accounts)
        dsu = DSU(n)

        
        # STEP 1: Froming account groups O(m)
        emailToAccount = {}
        for i, data in enumerate(accounts):
            for email in data[1:]:
                if email in emailToAccount: 
                    dsu.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i
        
        # STEP 2: Forming email groups  O(m)
        emailGroups = defaultdict(list)
        for email, groupIndex in emailToAccount.items():
            parent = dsu.find(groupIndex)
            emailGroups[parent].append(email)
        
        # STEP 3: Formatting the answer O(mlogm)
        result = []
        for accountIndex, emails in emailGroups.items():
            name = accounts[accountIndex][0]
            result.append([name] + sorted(emails))
        return result 


        
# C Update