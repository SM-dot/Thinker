class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        totalKeys = 0
        q = deque() # i , j, steps, current key status

        # key status = 00000 -> 0 means key not found, 1 means key found
        # let's say we find 'b'
        # Update procedure: 
        # 'b' - 'a' = 1
        # 000 OR 001 << 1 => 000 OR 010 <--- KEY STATUS
        # Handling lock: 
        # found 'C' 
        # 'C' - 'A' = 3
        # 110 = current key status 
        # 110 AND 100 = 1 we can move to this lock
        # When count of 1's in key status == total keys we know we have found our answer and simply return the number of steps 

        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "@":
                    q.append((i, j, 0, 0))
                    visited.add((i, j, 0)) # i, j, keyStatus 
                if grid[i][j] <= 'f' and grid[i][j] >= 'a':
                    totalKeys += 1
        
        while q:
            i, j, steps, keyStatus = q.popleft()

            if bin(keyStatus).count('1') == totalKeys:
                return steps 

            for dr, dc in directions:
                r =  i + dr
                c =  j + dc

                if r in range(n) and c in range(m) and grid[r][c] != "#":
                    ch = grid[r][c]

                    # key
                    if (ch >= "a" and ch <= "f"):
                        keyIndex = ord(ch) - ord("a")
                        newKey = keyStatus | 1 << keyIndex
                        if (r, c, newKey) not in visited:
                            q.append((r, c, steps + 1, newKey))
                            visited.add((r, c, newKey))
                    # lock
                    elif ch >= "A" and ch <= "F":
                        # checking if we have a key to that lock
                        keyIndex = ord(ch) - ord('A')
                        if keyStatus & 1 << keyIndex and (r, c, keyStatus) not in visited:
                            q.append((r, c, steps + 1, keyStatus))
                            visited.add((r, c, keyStatus))
                    # .
                    else:
                        if (r, c,keyStatus) not in visited:
                            q.append((r, c, steps + 1, keyStatus))
                            visited.add((r, c, keyStatus))
        return -1 

'''
Complexity	
Time	O(n * m * 2^K)
Space	O(n * m * 2^K)
'''