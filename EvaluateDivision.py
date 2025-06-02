# Leetcode Link: https://leetcode.com/problems/evaluate-division/?envType=study-plan-v2&envId=top-interview-150
# Category: DFS, Graphs, Recursion 

from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Evaluates division queries based on given equations using DFS traversal.
        - Python passes arguments by object-reference. For mutable objects (like lists), modifications inside
          a function affect the original object. For immutable objects (like floats, ints), each function call
          gets its own copy, so changes don't propagate back.
        - We use a one-element list `ans = [-1.0]` to simulate pass-by-reference for the result.
          This allows DFS to update the result "in-place" from within recursive calls.
        - The `product` variable is a float (immutable), so each DFS call receives its own copy of
          the current product of division values so far. No backtracking (undoing) is required
          after each recursive call, because Python naturally keeps each function call's local variables separate.
        """

        # Build graph as adjacency list: node -> [(neighbor, weight)]
        hm = defaultdict(list)
        values_bag = set()

        for i in range(len(equations)):
            num, denom = equations[i]
            val = values[i]

            values_bag.add(num)
            values_bag.add(denom)
            hm[num].append((denom, val))
            hm[denom].append((num, 1/val))  # reciprocal edge

        def dfs(src, dest, product, visited, ans):
            if src in visited:
                return
            visited.add(src)
            if src == dest:
                ans[0] = product
                return
            for neighbor, val in hm[src]:
                dfs(neighbor, dest, product * val, visited, ans)

        answer = []
        for src, dest in queries:
            if src not in values_bag or dest not in values_bag:
                answer.append(-1.0)
            else:
                visited = set()
                ans = [-1.0]  # mutable wrapper to carry result back through DFS
                dfs(src, dest, 1.0, visited, ans)
                answer.append(ans[0])

        return answer

# Git Ver
