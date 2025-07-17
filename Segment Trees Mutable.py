# LeetCode 307. Range Sum Query - Mutable
# Problem Link: https://leetcode.com/problems/range-sum-query-mutable/
# Category: Segment Trees, Binary Indexed Tree

class NumArray:

    def __init__(self, nums: List[int]):
        '''
        Using segment trees to optimize queries 
        Brute force time complexity: O(queries * n)
        Using segment trees time complexity: O(queries * logn)
        '''
        self.n = len(nums)
        self.segmentTree = [0] * (4 * self.n)
        
        # Building the segment tree
        # T.C: O(N)
        def buildTree(i, l, r):
            # Base Case: Reached a leaf node, cannot break down into further segments
            if l == r:
                self.segmentTree[i] = nums[l]
                return 
            mid = (l + r) // 2
            # build the tree on the left 
            buildTree(2*i + 1, l, mid)
            # build the tree on the right
            buildTree(2*i + 2, mid + 1, r)
            # After the tree is built now adding the sum of the ranges
                                # Left of node        Right of node
            self.segmentTree[i] = self.segmentTree[2 * i + 1] + self.segmentTree[2 * i + 2]
        
        buildTree(0, 0, self.n - 1)
        

    def update(self, index: int, val: int) -> None:
        '''
        Updating in segment trees means we would go down to a leaf node
        Just traversing based on which half the answer/ index we are looking for would lie in 
        '''
        # T.C: O(2logn) = O(logn) -> height of the tree traversed 
        def updateTree(index, val, i, l, r):
            # Reached a leaf node or the index where we need to update the val
            if l == r:
                self.segmentTree[i] = val
                return 
            mid = (l + r) // 2
            # look for in the left subtree
            if index <= mid:
                updateTree(index, val, 2*i + 1, l, mid)
            else:
            # look for index in the right subtree
                updateTree(index, val, 2*i + 2, mid + 1, r)
            # on the way back update the sums that were affected
            self.segmentTree[i] = self.segmentTree[2*i + 1] + self.segmentTree[2*i + 2]
        
        updateTree(index, val, 0, 0, self.n - 1)
        

    def sumRange(self, left: int, right: int) -> int:
        '''
        Going to be querying on our segment trees 
        TC: O(query * logn)
        In the worse case the left is a leaf node -> reaching this would take logn
        right is also a leaf node -> reaching this would take logn 
        thus in worse case its 2 logn which is better than o(n)
        '''
        def query(start, end, i, l, r):
            # condition 1: l and r are not in start to end range
            if (l > end or r < start):
                return 0
            
            # condition 2: l and r fall completely inside start to end range
            if ( l >= start and r <= end):
                return self.segmentTree[i]
            
            # condition 3: l and r partially inside the start to end range
            mid = (l + r) // 2
            # look in the left and right half of the tree 
            return query(start, end, 2 * i + 1, l, mid) + query(start, end, 2*i + 2, mid + 1, r)
        
        return query(left, right, 0, 0, self.n - 1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)