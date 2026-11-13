# Leetcode Problem: 1203. Sort Items by Groups Respecting Dependencies
# Leetcode Link: https://leetcode.com/problems/sort-items-by-groups-respecting-de
# Category: Graph, Topological Sort, DFS, BFS

'''
time complexity: O(n + m) where n is the number of items and m is the number of dependencies in beforeItems. This is because we are doing a topological sort on both the item-level and group-level graphs, which takes O(n + m) time.
space complexity: O(n + m) for the adjacency lists and indegree arrays used in the

        Ok, this is basically a toposort problem mainly. You should apply toposort in two places and sorting is not smallest to largest it is based on these paramters: 
        1. Sorted based on the groups
        2. Sorted based on the before array or the sequence

        so u need to follow a few steps: 
        1. Get indegrees for the items, like before array 
        2. Get indegrees for the groups themn 
        3. Then topo sort on the items based on before 
        4. then topo sort on the items based on the group from before itslef but now u are focussed on the groups 
        5. then take these 2 toposort and go over the topodort of the items and put them in lists of each of the group. 
        6. then go over the topo sort of the groups and put the lists in the result
'''
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        # 1. Assign each unassigned (-1) item its own unique group ID
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        adjItem = defaultdict(list)
        adjGroup = defaultdict(list)
        indegreesItems = [0] * n
        indegreesGroups = [0] * m

        # 2. Build both dependency graphs (item-level and group-level)
        for i in range(n):
            for prev in beforeItems[i]:
                adjItem[prev].append(i)
                indegreesItems[i] += 1

                groupI = group[i]
                groupPrev = group[prev]
                if groupI != groupPrev:
                    adjGroup[groupPrev].append(groupI)
                    indegreesGroups[groupI] += 1

        def topoSort(adj, indegrees):
            q = deque([i for i, deg in enumerate(indegrees) if deg == 0])
            result = []
            while q:
                node = q.popleft()
                result.append(node)
                for nextNode in adj[node]:
                    indegrees[nextNode] -= 1
                    if indegrees[nextNode] == 0:
                        q.append(nextNode)
            return result if len(result) == len(indegrees) else []

        # 3. Run topological sort on both graphs
        itemsTopo = topoSort(adjItem, indegreesItems)
        groupTopo = topoSort(adjGroup, indegreesGroups)

        if not itemsTopo or not groupTopo:
            return []

        # 4. Bucket sorted items into their respective groups
        groupResult = defaultdict(list)
        for item in itemsTopo:
            groupResult[group[item]].append(item)

        # 5. Flatten buckets according to the sorted group order
        result = []
        for grp in groupTopo:
            result.extend(groupResult[grp])

        return result
            

