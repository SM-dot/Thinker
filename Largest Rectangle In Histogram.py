# LeetCode 84. Largest Rectangle in Histogram
# Problem Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
# Category: Stack, Monotonic Stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        height [0, 3, 4, 5] and the next height is 1
        this means that we can no longer have a rectangle of height 5
        cause the new height is less. So we calculate the max area height 5
        could have had = height * (currentIndex(index of 1) - index for 5)
        We pop from the stack. Then we have 4 at the top, this is also greater
        than 1, so we calculate area for this height as well. Note that from a large height 
        we build the rectangle forwards till current index

        Now after you have popped values, you will notice your stack has [0]
        now before you put 1 notice that for all the large heights you popped you could extend your
        current height backwards and make a rectangle of width of the numbers till 1 and height 1
        In the stack we will be storing starting Index of height for that rectangle, height. 
        Thus you store 3'd height for 1 cause till there it could extend. 
        '''
        stack = [] # (starting index for rectangle of height h, hieght h)
        maxArea = 0
        n = len(heights)

        for currI, currH in enumerate(heights):
            start = currI
            while stack and stack[-1][1] > currH:
                index, height = stack.pop()
                # calculating area from starting index to current poitn => forwards
                maxArea = max(maxArea, height * (currI - index))
                start = index
            stack.append((start, currH))
        
        # all the backwards rectangles
        for i, h in stack:
            area = h * (n-i)
            maxArea = max(maxArea, area)
        
        return maxArea
