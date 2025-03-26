# Leetcode Link: https://leetcode.com/problems/non-overlapping-intervals/description/
# Category: Arrays, 2 pointer, Interval
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Think of this problem case by case.
        Tip: Solve it by picking any test case/ example

        our example: [1,2],[2,3],[3,4],[1,3]
        sort it: [1, 2], [1, 3], [2, 3], [3, 4] -> sorted based on start time 

        Note: compare 2 intervals at a time 

        Case 1: 
        when your end time of [1, 2] = 2 is <= start time of [1, 3]
        Example: [1, 2] [3, 4] => no overlap (simpler example to explain this case)

        Case 2:
        If we fail case 1 we know there is an overlap! Now what is left is to determine is 
        which interval to delete. We always want to delete the interval that is larger in size/ the one which is further in the number line if we have [1, 3] and [1, 7] we want to delete [1, 7] as it will contradict lesser intervals/ less chance of overlap in future 
          i.         j 
        [1, 2] and [1, 3]
        in this we see 2 <= 3 
        so delete [1, 3] by moving j to the next interval 

        Case 3: 
        [1, 5] and [2, 4]
        In this we see 5 >= 4
        so delete interval [1, 5] by moving i += 1 and j also += 1

        Let's code! 
        '''

        n = len(intervals)
        if n  == 1:
            return 0
        i = 0
        j = 1 
        answer = 0

        intervals.sort(key=lambda x: x[0])

        while (j < n):
            i_end = intervals[i][1]

            j_start = intervals[j][0]
            j_end = intervals[j][1]

            if (j_start >= i_end):
                i = j
                j += 1
            
            elif (i_end <= j_end):
                answer += 1
                j += 1

            elif (i_end >= j_end):
                answer += 1
                i = j
                j += 1
        return answer 
