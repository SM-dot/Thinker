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



class Solution:
    def longestPath(self, parent: list[int], s: str) -> int:
        '''
        okie tokie, so this one is very similar to max path sum. 

        Few things to note here is that this is not a tree so u just do not chekc left or right child. You have to check all the children paths. Now, if you are doing that how are you keepping track of which paths lead to the best answer, you need left and right equivalent. For that you keep longest and second longest number in memory and then send accordingly. 

        This is a gonna be a DFS, so O(V + E) is going to be the time and space complexity of this code. 
        
        Now lets code
        '''
        adj = defaultdict(list)
        n = len(parent)
        answer = ""

        def solve(node, parent):
            largest = ""
            secondLargest = ""
            nonlocal answer 
            
            for child in adj[node]:
                if child == parent: 
                    continue 

                getChildPath = solve(child, node)
                
                # it is very very important for our code to have this check after we have called the function on the child node cause what if in the child tree is where our longest path lies, so u are technically only skipping it if it is a adjacent, but u still need to excplore that tree if it makes sense 
                if s[child] == s[node]:
                    continue

                if len(getChildPath) > len(secondLargest):
                    secondLargest = getChildPath
                
                if len(secondLargest) > len(largest):
                    secondLargest, largest = largest, secondLargest
                
            case1 = s[node]
            case2 = s[node] + largest
            case3 = largest[::-1] + s[node] + secondLargest

            current_best = max([case1, case2, case3], key=len)
            if len(current_best) > len(answer):
                answer = current_best
            return case2
                

        for i in range(1, n):
            u = i
            v = parent[i]

            adj[u].append(v)
            adj[v].append(u)

        solve(0, -1)
        print(answer)
        return len(answer)
