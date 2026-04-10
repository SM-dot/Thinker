# Leetcode 206: Reverse Linked List
# Problem Link: https://leetcode.com/problems/reverse-linked-list/
# Category: Linked List
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) since we are using only a constant amount of extra space

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Need three pointers for this one, one of them is going to be prev node another one curr and then another one is going to be next.
        '''

        prevNode = None 
        curr = head 


        while curr:
            realNext = curr.next 
            curr.next = prevNode 
            prevNode = curr 
            curr = realNext
        
        return prevNode
