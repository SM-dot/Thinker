# Leetcode link: https://leetcode.com/problems/get-watched-videos-by-your-friends/?envType=problem-list-v2&envId=9id9smj2
# Category: Graphs, BFS 
from collections import defaultdict, deque
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        """
        Approach:
        - This problem involves finding all friends at a specific level in an unweighted friendship graph
          and collecting the videos they watched.
        - We use Breadth-First Search (BFS) starting from the given person `id` to explore the graph level by level.
        - Once we reach the desired level `level`, we stop and collect videos watched by those friends.
        - We count the frequency of each video using a frequency map.
        - Then, we bucket the videos by their frequencies and sort each bucket alphabetically.
        - Finally, we return a list of videos sorted first by frequency (ascending), then by name (lexicographically).
        """
        
        n = len(friends)
        q = deque()
        q.append(id)
        c_level = 0
        visited = set()
        visited.add(id)

        while q:
            freq_map = defaultdict(int)
            size = len(q)
            for i in range(size):
                element = q.popleft()
                for video in watchedVideos[element]:
                    freq_map[video] += 1
                
                for nextFriend in friends[element]:
                    if nextFriend not in visited:
                        q.append(nextFriend)
                        visited.add(nextFriend)
            
            if level == c_level:
                break 
            c_level += 1
        
        buckets = [[] for _ in range(size + 1)]
        for k, v in freq_map.items():
            buckets[v].append(k)
        
        answer = []
        index = 0 
        print(freq_map)
        while (index <= size ):
            if not buckets[index]:
                index += 1
                continue 
            if len(buckets[index]) > 1:
                buckets[index] = sorted(buckets[index])
                for item in buckets[index]:
                    answer.append(item)
            else:
                answer.append(buckets[index][0])
            index += 1
        
        return answer 
