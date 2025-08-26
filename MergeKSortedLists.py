# Leetcode Problem 23. Merge k Sorted Lists
# Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/
# Category: Linked List, Divide and Conquer, Heap, Merge Sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        need to merge k linked lists 
        think about how ull merge two linked lists 
        merge l1 and l2, -> get ans
        ans and l3 merged 
        so you can have a function that merges two lists
        and keep on doing this 

        l1
        1 -> 4 -> 5
        2 -> 6 
        l2

        compare l1 and l2
        recursion will handle the rest of the merging 


        base cases:
        if l1 == null:
            return l2
        if l2 == null:
            return l1
        if l1 <= l2:
            l1.next = will hold the rest of the merged list merge(l1.next, l2)
            you will return l1 
        else:
            l2.next = merge(l2.next, l1
            return l2 
        Can also do merge 2 lists and then build off that here 


        [l1, l2, l3, l4, l5]
        merge like merge sort 
        group them 
        merge x and y 
         x              y
        [l1, l2, l3] - [l4, l5]
        [l1, l2] [l3]   [l4] [l5]
        ....            if start of [l4] == end of [l4] return the list as is


        we break it up this way cause if we merge l1 with l2 then l2 with l3 we will be going through each list and remerging multiple nodes 
        if total number of lists = k
        number of nodes in each list = n 
        then the T.C for soemthing like that would be = O(n*k)

        However, if we partition and break it up then:
        Merging 2 lists is still O(n)
        However, instead of going through and merging linearly 
        we are breaking it down into a tree of height O(log k)
        Thus the new time complexity is O(log k * n)

        Now let's code!! 
        '''

        def merge2lists(l1, l2):
            if not l1:
                return l2
            
            if not l2:
                return l1
            
            if l1.val <= l2.val:
                l1.next = merge2lists(l1.next, l2)
                return l1
            else:
                l2.next = merge2lists(l2.next, l1)
                return l2
        

        def partition(start, end):
            if start > end: 
                return 

            if start == end:
                return lists[start]

            mid = start + (end - start) // 2
            one = partition(start, mid)
            two = partition(mid + 1, end)
            return merge2lists(one, two)
        
        return partition(0, len(lists) - 1)


        