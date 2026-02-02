# Leetcode Problem Link: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
# Leetcode Problem: 1962. Remove Stones to Minimize the Total
# Category: Array, Heap (Priority Queue), Greedy
# Difficulty: Medium

# Time Complexity: O((n + k) log n), where n is the number of piles and k is the number of operations. Building the max heap takes O(n) time, and each of the k operations involves removing and adding an element to the heap, which takes O(log n) time.
# Space Complexity: O(n) for storing the max heap.
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        '''
        So we should find the maximum element in the array and then go ahead and apply the k operation. 
        One thing would be that we sort it. However, note that after applying the operation the array would modify. You would need to sort it at each step then and thta would increase the TC. 

        That is why use a max heap, and each time u edit a numbe ru add it to the heap. 

        Final Algorithm:
        1. Add all numbers to the heap, we want a max heap and Python does not support that so instead use a min heap and make eveything negative in it. 
        2. Run the loop k times. Each time remove the element from the top of the heap. apply the operation and add it back to the heap
        3. Return the sum 
        Time compelxity: 
        Adding eveythign in the heap: 
        If we used the hapify function directly then O(n)
        Otherwise adding eberything one by one taken O(nlogn)
        then removing and adding k times so klogn 
        as push and pop on heap takes logn time
        Now let's code! 
        '''
        heap = []
        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for _ in range(k):
            element = -heap[0]
            heapq.heappop(heap)
            element_modify = element - floor(element/2)
            heapq.heappush(heap, -element_modify)

        answer = 0
        for num in heap:
            answer += (-num)
        return answer 