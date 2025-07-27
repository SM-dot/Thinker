# Leetcode 2246. Longest Path with Different Adjacent Characters
# Problem Link: https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
# Category: Graph, DFS


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        '''
        Very similar to binary path sum
        Usually while fidning the max path sum you have 3 cases
        1. left path + root + right path 
        2. max(left, right) + root
        3. root

        However, this is a graph and you do not just have left or right sidees, you have multiple nodes. Thus instead of comparing the left and right path, you can compare the longest and the second longest path. 
        '''
        result = 0
        adj= defaultdict(list)
        n = len(parent)
        for i in range(1, n):
            u = i
            v = parent[i]
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            nonlocal result
            longest = 0
            secondLongest = 0

            for child in adj[node]:
                if child != parent: 
                    childPathLength = dfs(child, node)
                    # making sure adjacent nodes are not same 
                    if s[child] != s[node]:
                        if childPathLength > secondLongest:
                            secondLongest = childPathLength
                        
                        if secondLongest > longest:
                            secondLongest, longest = longest, secondLongest
            
            case1 = longest + 1 + secondLongest #cannot send this value up cause its a complete path, if we send it up it will be a fork 
            case2 = longest + 1
            case3 = 1

            result = max(result, case1, case2, case3)
            return max(case2, case3)

        dfs(0, -1)
        return result 