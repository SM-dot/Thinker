# LeetCode 239. Sliding Window Maximum
# Problem Link: https://leetcode.com/problems/sliding-window-maximum/
# Category: Sliding Window, Deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        For this question, we can use a monotonic q
        What's a monotonic q? 
        It is a queue which can store numbers in increasing or decreasing order. 

        How does that help? 
        If we keep track of the numbers in the q, we can get the max value for each subarray. 

        We need to find the max value in each window => we should use a decreasing monotonic q. Why? 
        decreasing monotonic q:
        [5, 4, 3]
        the front of the queue would give us the max seen for each window.
        Time Complexity: O(n)
        Space Complexity: O(n)

        NOTE:
        In a monotonic q, you actaully store the indices, this way you can also access the elements. Since in this question we have a window size of k, make sure your q never has an element outside the winow size. If it does simply pop. A check would be q[0] #front of q < i - k then pop

        Now let's code! 

        [1,3,-1,-3,5,3,6,7]
        0. 1 2 3
        '''
        q = deque()
        answer = []
        n = len(nums)

        # building a monotonic decreasing queue
        for i in range(n):
            
            # making sure the q only has elements in the q with valid indexes for the window range
            while q and q[0] <= i - k:
                q.popleft() #removing elements from the back of the q 
            
            while q and nums[q[-1]] < nums[i]: 
                q.pop() # removing elements from the right of the q or front
            q.append(i) # MAKE SURE YOU STORE INDEX AND NOT THE VALUE 

            # this check ensure we have a k sized window 
            if i >= k - 1:
                answer.append(nums[q[0]]) #the element first from the left of the quue would be the largest which is the maximum for that subarray, thus storing it in the answer REMEMBER TO APPEND THE VALUE NOT THE INDEX HERE 
        
        return answer 

            