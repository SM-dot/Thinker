# LeetCode Problem Link: https://leetcode.com/problems/merge-intervals/
# LeetCode Problem: 56. Merge Intervals
# Category: Array, Sorting

# Time Complexity: O(N log N) due to sorting the intervals.
# Space Complexity: O(N) for the result list in the worst case when no intervals overlap

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        [[1,3],[2,6],[8,10],[15,18]]
        1 2 3 4 5 6 7 8 9 10 ... 15 18
        -----
          ---------
                    ---------  
                                -----
        '''
        # make sure the list of the intervals is sorted first 
        # then have starting and ending pointers
        # if the current ending pointer is greaterv that the starting pointer of the next interval 
        # then go ahead and change the interval, the ending to be the max of the two endings 
        # in the case the current ending is less than the new staring then go ahead and add the current inetrvals start and end, gice start and end this new interval values

        intervals.sort()
        n = len(intervals)
        result = []

        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, n):
            nextStart = intervals[i][0]
            nextEnd = intervals[i][1]
            if nextStart <= end: 
                end = max(end, nextEnd)
            
            else: 
                result.append([start, end])
                start = nextStart
                end = nextEnd
            

        result.append([start, end])
        
        return result