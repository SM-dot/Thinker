# LeetCode Problem Link: https://leetcode.com/problems/seat-reservation-manager/
# LeetCode Problem: 1845. Seat Reservation Manager
# Category: Array, Heap Data Structure, Design
# Difficulty: Medium


class SeatManager:
    '''
    Can be solved with a regular array but that takes O(n) time. If we use a heap pushing everything in the heap takes at least O(nlogn) push n into logn

    But if we keep a marker then we do not need to push n times only logn operations are gonna take place. 

    Now, let's code!
    '''
    def __init__(self, n: int):
        self.seatMarker = 1
        self.heap = [] # min heap
        

    def reserve(self) -> int:
        if self.heap: 
            return heapq.heappop(self.heap)
        
        seatOccupied = self.seatMarker
        self.seatMarker += 1
        return seatOccupied
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)