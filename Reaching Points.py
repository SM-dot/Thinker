# Leetcode Link: https://leetcode.com/problems/reaching-points/description/
# Category: Math, Greedy, Recursion, Graphs
# Difficulty: Hard


# OPTIMIZED SOLUTION 
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        Instead of working forward, work backward 

        if tx > ty then 
        (tx - ty, ty) -> till you reach sx and sy to further optimize this do tx%ty
        example (23, 5) = target and (3, 5) = starting
        (23 - 5, 5) = (18, 5) -> (13, 5) -> (8, 5) -> (3, 5) reached!
        instead just do (23%5, 5) == (3, 5) simple one step 


        2 main cases 
        tx > ty:
            tx = tx % ty

        ty > tx: 
            ty = ty % tx
        
        however, if ty == sy that means we can only change tx 
        to know id changing tx will yield in an answer we need to do 
        (tx - sx) % y 
        example:
        target = (22, 5) start = (3, 5)
        ty == sy 
        (22 - 3) % 5 != 0 means we will never reach sx
        4

        example: 
        target = (23, 5) start = (3, 5)
        ty == sy
        (23 - 3) % 5 == 0 
        can reach this point!


        Dry run: 
        (3, 5) = target (1, 1) = start
        ty > tx:
            tx != sx so we are good
            ty = ty%tx = 5%3 = 2
        
        (3, 2) = target (1, 1) = start
        tx > ty:
            ty != sy so we are good
            tx = tx%ty = 3%2 = 1
        
        (1, 2) = taregt (1, 1) = start
        ty > tx:
            tx == sx:
                so only one check left 
                ty = (ty - tx) % ty == 0
                      (2 - 1) % 1 == 0
                thus true!
        
        Time complexity = O(log(max(tx, ty))) cause we go on reducing it
        Space complexity = O(1) no extra space taken! 
        Much better solution that BFS brute force :)

        Reason: When ty == sy, you need to check if tx can be reduced to sx by repeatedly subtracting ty (i.e., (tx - sx) % ty == 0). Similarly, when tx == sx, check if ty can be reduced to sy by subtracting tx (i.e., (ty - sy) % tx == 0).
Example:

Input: sx = 3, sy = 5, tx = 22, ty = 5
When ty == sy, your code checks (tx - ty) % ty = (22 - 5) % 5 = 17 % 5 = 2, which returns False. But it should check (tx - sx) % ty = (22 - 3) % 5 = 19 % 5 = 4, which is also incorrect in your code. The correct check should align with the modulo logic, but the subtraction is off.


        Now, let's code! 
        '''
        while tx >= sx and ty >= sy:

            if tx == sx and ty == sy:
                return True 
            
            if tx > ty:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx = tx % ty
            else:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty = ty % tx
        
        return tx == sx and ty == sy


# BRUTE FORCE BFS SOLUTION (TLE)
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        Instead of working forward, work backward 

        if tx > ty then 
        (tx - ty, ty) -> till you reach sx and sy to further optimize this do tx%ty
        example (23, 5) = target and (3, 5) = starting
        (23 - 5, 5) = (18, 5) -> (13, 5) -> (8, 5) -> (3, 5) reached!
        instead just do (23%5, 5) == (3, 5) simple one step 


        2 main cases 
        tx > ty:
            tx = tx % ty

        ty > tx: 
            ty = ty % tx
        
        however, if ty == sy that means we can only change tx 
        to know id changing tx will yield in an answer we need to do 
        (tx - sx) % y 
        example:
        target = (22, 5) start = (3, 5)
        ty == sy 
        (22 - 3) % 5 != 0 means we will never reach sx
        4

        example: 
        target = (23, 5) start = (3, 5)
        ty == sy
        (23 - 3) % 5 == 0 
        can reach this point!


        Dry run: 
        (3, 5) = target (1, 1) = start
        ty > tx:
            tx != sx so we are good
            ty = ty%tx = 5%3 = 2
        
        (3, 2) = target (1, 1) = start
        tx > ty:
            ty != sy so we are good
            tx = tx%ty = 3%2 = 1
        
        (1, 2) = taregt (1, 1) = start
        ty > tx:
            tx == sx:
                so only one check left 
                ty = (ty - tx) % ty == 0
                      (2 - 1) % 1 == 0
                thus true!
        
        Time complexity = O(log(max(tx, ty))) cause we go on reducing it
        Space complexity = O(1) no extra space taken! 
        Much better solution that BFS brute force :)
        Now, let's code! 
        '''
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
                
            if tx == sx and ty == sy:
                return True 
            
            if tx > ty:
                if ty == sy:
                    return (tx - ty) % ty == 0
                tx = tx % ty
            else:
                if tx == sx:
                    return (ty - tx) % tx == 0
                ty = ty % tx
        
        return tx == sx and ty == sy