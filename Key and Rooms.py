# LeetCode 841. Keys and Rooms
# Problem Link: https://leetcode.com/problems/keys-and-rooms/   
# Category: Graph, BFS, DFS


class Solution:
    '''
    Input: List of rooms, each room contains keys to other rooms
    Operations:
    - Use BFS to explore all reachable rooms starting from room 0
    - Keep track of visited rooms to avoid cycles
    Output: True if all rooms can be visited, False otherwise
    T.C: O(N + E) where N is number of rooms and E is number of keys
    S.C: O(N) for the visited set and queue
    Can also be solved using DFSs
    '''
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        n = len(rooms)
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            room = q.popleft()

            for nextRoomKey in rooms[room]:
                if nextRoomKey not in visited: 
                    q.append(nextRoomKey)
                    visited.add(nextRoomKey)
        
        return len(visited) == n