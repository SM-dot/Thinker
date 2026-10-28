# Leetcode Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Leetcode Name: Merge Two Sorted Lists
# Category: Linked List, Recursion, Two Pointers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Time Complexity: O(n + m) where n is the length of list1 and m is the length of list2
# Space Complexity: O(1) as we are not using any extra space except for the
# answer list which is the output and we are not using any extra space for recursion or any

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        answer = ListNode()
        dummy = answer

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2 
                list2 = list2.next
            
            dummy = dummy.next 
        
        if list1: 
            dummy.next = list1
        
        if list2:
            dummy.next = list2
        
        return answer.next