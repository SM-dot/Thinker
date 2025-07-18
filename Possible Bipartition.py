# LeetCode 886. Possible Bipartition
# Problem Link: https://leetcode.com/problems/possible-bipartition/
# Category: Graph, BFS, DFS, Union Find

class Solution:
    '''
    Input: n people, dislikes pairs
    Operations:
    - Build an adjacency list to represent the graph of dislikes            
    - Use BFS to try and color the graph using two colors (0 and 1)
    - If we find a conflict (two adjacent nodes with the same color), return False
    - If we can color the graph without conflicts, return True
    Output: True if possible to bipartition, False otherwise
    T.C: O(N + E) where N is number of people and E is number
    of dislike pairs
    S.C: O(N + E) for the adjacency list and group array
    Can also be solved using DFS or Union-Find
    '''
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Build adjacency list
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        # Initialize group array: -1 means unassigned, 0 or 1 means assigned to a group
        group = [-1] * (n + 1)
        
        # Process each unvisited node to handle disconnected components
        for person in range(1, n + 1):
            if group[person] == -1:  # If node is unvisited
                # Start BFS from this node
                q = deque([person])
                group[person] = 0  # Assign to group 0 arbitrarily
                
                while q:
                    curr_person = q.popleft()
                    curr_group = group[curr_person]
                    
                    # Check all neighbors (people who dislike curr_person)
                    for next_person in adj[curr_person]:
                        if group[next_person] == -1:  # Unvisited neighbor
                            group[next_person] = 1 - curr_group  # Assign opposite group
                            q.append(next_person)
                        elif group[next_person] == curr_group:  # Conflict: same group
                            return False
        
        return True