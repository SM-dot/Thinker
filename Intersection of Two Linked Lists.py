# Leetcode Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Leetcode Name: Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Time Complexity: O(N + M) where N is the length of list A and M is the length of list B
# Space Complexity: O(N) where N is the length of list B, we are storing

# optimized solution is to use two pointers and traverse both lists, 
# when one pointer reaches the end of its list, it starts traversing the other list. 
# This way, both pointers will meet at the intersection point if there is one.
# code for optimal solution:
def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA  # or pointerB, they are equal at this point

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        storeBNodes = set()

        dummyB = headB
        while dummyB: 
            storeBNodes.add(dummyB)
            dummyB = dummyB.next 
        

        # Now traverse through A and see if any of the B values are there then return that node 
        dummyA = headA 
        while dummyA:
            if dummyA in storeBNodes: 
                return dummyA 
            dummyA = dummyA.next 
        
        return None 
