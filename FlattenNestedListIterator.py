# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Time Complexity: O(n), where n is the total number of integers in the nested list. In the worst case, we may need to traverse all elements to flatten the list.
# Space Complexity: O(n) for the stack used to store the nested integers. In the worst case, if the nested list is deeply nested, the stack can grow to the size of the
# total number of integers in the list.

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.s = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.s.append(nestedList[i])
    
    def next(self) -> int:
        return self.s.pop().getInteger()
    
    
    def hasNext(self) -> bool:
        while self.s:
            current = self.s[-1]
            if current.isInteger():
                return True
            current = self.s.pop()
            n = current.getList()
            for i in range(len(n) - 1, -1, -1):
                self.s.append(n[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())