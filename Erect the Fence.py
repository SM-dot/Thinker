# Leetcode Problem: 587. Erect the Fence
# Link: https://leetcode.com/problems/erect-the-fence/
# Difficulty: Hard
# Category: Geometry, Convex Hull


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        '''
        slope between two point(x1, y1) and (x2, y2):
        m = y2 - y1
            -------
            x2 - x1
        
        if we have three points 
        (x1, y1)  m1  (x2, y2)  m2  (x3, y3)
        if the slope m2 > m1 => counterclockwise direction
        if the slope m2 < m1 => clockwise direction 
        the upper points should be in a clockwise direction
        the lower points should be in a counterclockwise direction

        if we have 3 points, p1, p2 have been in clockwise and now the pattern changes, we remove the point from our list. 
        Similarly, even for the lower point. 

        In the end, we will combine the points in lower and upper and remove the duplicates. 

        In order to make sure the order we are moving in is correct we also need to make sure the input points are sorted. 

        Equation to check clockwise: 
        (x1, y1)  m1  (x2, y2)  m2  (x3, y3)

        y3 - y2/ x3 - x2 > y2 - y1/ x2 - x1
        (y3 - y2/ x3 - x2) - (y2 - y1/ x2 - x1) > 0
        cross multiply, the divisor multiplies with 0 if we move it back to the right. Therefore the main equation is: 

        (y3-y2)(x2-x1) - (y2-y1)(x3 - x2) > 0 => clockwise

        Time Complexity: O(nlogn)
        explanation: Sorting the points takes O(n log n) time. The while loops inside the for loop each run in O(n) time in total, as each point is added and removed at most once. Therefore, the overall time complexity is dominated by the sorting step, resulting in O(n log n).
        Space Complexity: O(n)
        Now, let's code!
        '''

        def clockwise(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return  (y3-y2)*(x2-x1) - (y2-y1)*(x3 - x2)
        
        trees.sort()
        upper = []
        lower = []

        for p in trees:
            # keep on removing the points till they are not clockwise
            while len(upper) > 1 and clockwise(upper[-2], upper[-1], p) < 0:
                upper.pop()
            while len(lower) > 1 and clockwise(lower[-2], lower[-1], p) > 0:
                lower.pop()
            
            upper.append(tuple(p))
            lower.append(tuple(p))
        
        return list(set(upper + lower))
            
        