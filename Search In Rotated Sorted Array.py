# Leetcode Problem: 33. Search in Rotated Sorted Array
# Leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Leetcode Problem Name: Search in Rotated Sorted Array


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]
        # we want to do a binary search in the array before the pivot index
        # then we want to do a binary search in the array after the pivot index
        # finding pivot index basically means finding the smallest element in a rotated sorted array

        # overall T.C: O(log n)
        # explanation of TC:
        # finding pivot index: O(log n)
        # binary search on left side: O(log n)
        # binary search on right side: O(log n)
        # overall: O(3 log n) = O(log n)    
        # S.C: O(1)

        n = len(nums)

        def pivotIndex():
            # we want to find the smallest number in the array
            # [5 6 7 1 2]
            # mid = 7 index 7 > 2 implies that this side is not sorted so search here
            # l = mid + 1
            # if this side is sorted 
            # then r = mid cause mid could be the answer 
            # key thing to note here is that while l < r is the condition and not l <= r becuase then we will keep on getting r = mid all the time
            l = 0
            r = n - 1
            while l < r:
                mid = l + (r - l)//2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
            return r 
                
        
        def binSearch(l, r):
            idx = -1 

            while l <= r:
                mid = l + (r - l)//2
                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return idx 
        
        index = pivotIndex()
        leftResult = binSearch(0, index - 1)
        if leftResult != -1:
            return leftResult
        return binSearch(index, n - 1)

        