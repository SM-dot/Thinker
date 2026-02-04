class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        So we need to start whenever the start time is. However, the enqueue time and processing times could vary. 
        You need to sort the input. However, later on u also need to give th eoutput based on the task index. Therefore create a new data structure which has the enqueue time, processing time and the index of the task. 

        you start with current time is 0.
        You go through each task in the list or till the q is empty

        you see is my current time < the task and our heap is empty, if yes that means that we have not added our first task. So we update current time with the first task time. 

        in our heap we add all the tasks that have already arroved which means that takss with time <= current time 

        you then take the current task which is at the top of the heap cause this is the one that has the shortest processing time and index. Note this means that the heap has the processing time and the index

        you remove the top of the heap. 
        you add it to the result 
        you update the current time to the time of this task that you removed ending

        Time complexity: O(N log N) where N is the number of tasks. This is due to the initial sorting of the tasks and the heap operations.
        Space complexity: O(N) for storing the tasks and the heap.
        '''
        
        allTaskInfo = [] 
        for i in range(len(tasks)):
            allTaskInfo.append(tasks[i] + [i])

        sortedTasks = sorted(allTaskInfo)

        currTime = 0 
        idx = 0
        n = len(tasks)
        heap = []

        # even if we have gone through all tasks we still need to remove tasks from the q that are scheduled 
        result = []
        while heap or idx < n:
            if not heap and currTime < sortedTasks[idx][0]:
                currTime = sortedTasks[idx][0]
            
            while idx < n and sortedTasks[idx][0] <= currTime: 
                heapq.heappush(heap, (sortedTasks[idx][1], sortedTasks[idx][2]))
                idx += 1
            
            processDuration, processIndex = heapq.heappop(heap)
            currTime += processDuration
            result.append(processIndex)
        return result