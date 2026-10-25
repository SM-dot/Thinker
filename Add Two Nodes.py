# Leetcode Name: Add Two Numbers
# Leetcode Link: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        answerNode = ListNode()
        answer = answerNode

        while l1 or l2 or carry: 
            total = carry 
            if l1: 
                total += l1.val
                l1 = l1.next 
            
            if l2: 
                total += l2.val
                l2 = l2.next
            
            answer.next = ListNode(total % 10)
            answer = answer.next
            carry = total // 10
        
        return answerNode.next
        