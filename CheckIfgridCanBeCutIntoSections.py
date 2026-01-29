# LeetCode Problem Link: https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections-with-each-section-having-equal-number-of-rectangles/
# LeetCode Problem: 2565. Check if Grid Can Be Cut Into Sections With Each Section Having Equal Number of Rectangles
# Category: Array, Sorting, Greedy, Intervals
# Difficulty: Medium


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        '''
        Extremely fun problem: 
        Uses merge intervals cleverly. 

        So split the problem in two parts:
        can I make any vertical cuts?
        can I make any horizontal cuts? 

        now how do we decide vertical cuts:
        we see that we are not cutting through any rectangl. This means that are cut needs to be outside a rectangle or else the rectangle will be in 2 sections. Therefore we see the width of the rectangle. 
        get all the width of the rectangles it would be [x1, x2], [a1, a2], [b1, b2], etc
        Then you find how many of these rectangles overlap. Once you have combined all the overlaps, you will have the intervals where u cannot make a line. if you have one interval => cannot make any cut. You need atleast 2 intervals to make a cut. 

        Similarly for horizontal cuts you are looking at the y axis.

        The question asks if we can make any 2 cuts. 
        number of cuts = number of merged intervals - 1 
        therefore if horizontal and vertical individually is >= 2 then return True else False. 
        Codestroywithmik cchekc if horizontal intervals or vertical intervals are atleast 3 in size. 

        Time complexity: 
        sorting the interval lists = O(nlogn)
        Merging the inerval = O(n)
        Total = O(nlogn)
        Space complexity: O(n) for the interval lists.

        Now let's code! 
        '''
        x_intervals = []
        y_intervals = []

        for x1, y1, x2, y2 in rectangles:
            x_intervals.append([x1, x2])
            y_intervals.append([y1, y2])
        
        def mergeIntervals(intervals):
            intervals.sort()
            print("after sorting: ", intervals)
            start = intervals[0][0]
            end = intervals[0][1]
            n = len(intervals)
            result = []

            for i in range(1, n):
                nextStart = intervals[i][0]
                nextEnd = intervals[i][1]

                if end > nextStart:
                    end = max(end, nextEnd)
                
                if end <= nextStart:
                    result.append([start, end])
                    start = nextStart
                    end = nextEnd
            
            result.append([start, end])
            print(result)
            return len(result) - 1
        
        verticalCuts = mergeIntervals(x_intervals)
        print(verticalCuts)
        horizontalCuts = mergeIntervals(y_intervals)
        print(horizontalCuts)

        return verticalCuts >= 2 or horizontalCuts >= 2
        