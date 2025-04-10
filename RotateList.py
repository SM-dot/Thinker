# Leetcode Link: https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
# Category: LinkedLists 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # basically u want to identify a break point - this is a simple pattern problem, once k in in the length of your list you want to break it at k. 
        # 1->2->3->4->5 k = 2
        # breakpoint 3->
        # this means we need to know the length to find the breakpoint 
        # once we find the length we will also know the tail
        # the tail will be atached to the old head 
        # the new head would be the node 3->this node
        # the node pointing after the breakpoint 
        # in order to find the breakpoint we need to traverse length - k - 1 times down the list
        # T.C: O(n)
        # S.C: O(1)
        # Let's code! 

        start = head
        length = 1

        if not head:
            return head
            
        while(start.next != None):
            start = start.next
            length += 1
        
        # the start now is actaully the tail 
        breakp = head
        k = k % length 
        # edge case: even k rotations, means the list will be in its original form
        if k == 0:
            return head 
        for i in range(length - k - 1): 
            breakp = breakp.next
        
        newHead = breakp.next
        breakp.next = None
        start.next = head
        return newHead 

