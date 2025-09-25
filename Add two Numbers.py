# Leetcode Problem: 2. Add Two Numbers
# Link: https://leetcode.com/problems/add-two-numbers/
# Difficulty: Medium


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Explanation:
        We will traverse both linked lists simultaneously, adding corresponding nodes along with any carry from the previous addition.
        If one list is shorter, we treat its missing nodes as 0.
        We create a new linked list to store the result, and if there's a carry left after processing both lists, we add a new node for it.
        1. Initialize a dummy head for the result linked list and a pointer to traverse it.
        2. Initialize a variable to keep track of carry (initially 0).
        3. Loop through both linked lists until both are fully traversed and there's no carry left.
        4. For each pair of nodes (or 0 if a list is exhausted), calculate the sum and determine the new digit and carry.
        5. Create a new node with the calculated digit and append it to the result list.
        6. Move the pointer of the result list forward.
        7. Finally, return the next node of the dummy head, which is the start of the resultant linked list.
        Time Complexity: O(max(m, n)) where m and n are the lengths of the two linked lists.
        Space Complexity: O(max(m, n)) for the new linked list.

        explaining carry:
        carry = s // 10
        This line calculates the carry for the next iteration. The carry is determined by performing integer division
        of the sum (s) by 10. If the sum is 10 or greater, carry will be 1 (indicating that we need to carry over 1 to the next
        higher place value). If the sum is less than 10, carry will be 0 (indicating that there's no carry over).
        1. If s = 15, then carry = 15 // 10 = 1
        2. If s = 9, then carry = 9 // 10 = 0
        3. If s = 23, then carry = 23 // 10 = 2
        4. If s = 345, then carry = 345 // 10 = 34
        5. If s = 0, then carry = 0 // 10 = 0
        6. If s = 10, then carry = 10 // 10 = 1
        7. If s = 99, then carry = 99 // 10 = 9
        This carry value is then used in the next iteration of the loop to be added to the sum of the next pair of
        '''
        carry = 0
        answer = ListNode()
        dummy = answer

        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            
            if l2:
                s += l2.val
                l2 = l2.next
            

            s += carry
            fillVal = s % 10
            carry = s // 10
            dummy.next = ListNode(fillVal)
            dummy = dummy.next
        
        return answer.next
        


        