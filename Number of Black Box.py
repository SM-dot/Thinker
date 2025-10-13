# Leetcode Problem: 2319. Number of Black Blocks
# Link: https://leetcode.com/problems/number-of-black-blocks/
# Difficulty: Medium
# Category: Hashmap, Simulation, Matrix


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # Since the grid can be very big, we cannot traverse on the grid because of time and space constraints. 
        # Instead we need to kind of reverse engineer the problem 
        # From our coordinates figure out which blocks have how many cells
        # So for each black colored coordinate, find out all the boxes it is part of. Don't overthink it - just check (x - 1, y - 1), (x - 1, y), (x, y - 1) and (x, y) if the modified coordinates within range then all ok. Now for marking boxes, make sure each coordinate translates to a number. So our grid is going to be numbered 0, 1 .... To get the corresponding number to the cell there is a simple formula: x* number of columns + y
        # Next in the end from the hashmap update results. For blocks with 0 blacks, just do m - 1 * n -1 (total blocks) - len(map)
        # Now let's code! 

        # Time Complexity: O(N)
        # Space Compelxity: O(N)


        result = [0] * 5
        boxMap = defaultdict(int)

        for x, y in coordinates:
            # x - 1, y - 1 
            if (x - 1 >= 0 and y - 1 >= 0):
                boxMap[((x - 1) * n) + (y-1)]  += 1

            # x - 1, y
            if (x - 1 >= 0 and y < n - 1):
                boxMap[((x - 1) * n) + y]  += 1
            
            # x, y - 1
            if (y - 1 >= 0 and x < m - 1):
                boxMap[(x * n) + (y-1)]  += 1
            
            # x , y
            if (x < m - 1 and y < n - 1):
                boxMap[(x * n) + y]  += 1
        
        for k, v in boxMap.items():
            result[v] += 1
        
        result[0] = ((n - 1) * (m - 1)) - len(boxMap)
        return result 


# Brute Force: 
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # array index = number of black boxes 
        # keep an array

        result = [0] * 5
        coordinates = set([tuple(coord) for coord in coordinates])

        def checkBox(i, j):
            # returns the number of black boxes in it 
            count = 0
            if (i + 1, j + 1) in coordinates:
                count += 1
            if (i + 1, j) in coordinates:
                count += 1
            if (i, j + 1) in coordinates:
                count += 1
            if (i, j) in coordinates:
                count += 1
            return count


        for i in range(m - 1):
            for j in range(n - 1):
                result[checkBox(i, j)] += 1
        
        return result 
        