# Leetcode: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Leetcode Problem Name: Median of two sorted Arrays

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # we can put everything in one array and then find median but that is O(n) time and O(n) soace as well 
        # so to optimise, we are lookign for a solution that works in O(logn) time and space 
        # Binary Search is the answer!!!! 
        # We use binary search in identifying how many elements of the smaller array between n1 and n2 dow e want to include in our left partition 

        # Understanding partitions: 
        # our total array length will be n + m 
        # we divide a total array in 2 halfs using this formula: (n + m + 1) / 2
        # this evenly divides the array in 2 halfs for even and odd numbers. In case of odd numbers the left half is larger 


        # In our left partition if we have x elements of nums1 it means that we have (n + m + 1)/2 - x number of elements of nums 2 

        # in order to make sure, we have the correct sorted partitions 
        # check if the largest number of n1 in left side < smallest number of n2 in right side
        # a1 a2 a3 |  a4 a5
        # b1 b2    |  b3 b4

        # here checking a3 < b3 and b2 < a4 
        # obviously cause we have sorted arrays, a3 < a4 && b2 < b3 so not checking for that 

        # in the case a3 > b3 then we need to take fewer elements in the left partition from nums1 so on our binary serach we move left 

        # a1 a2    |  a3 a4 a5
        # b1 b2    |  b3 b4

        # once we know it is sorted in the correct method
        # if m+n is odd 
        # return max(a2, b2)
        # if m+n is even
        # find max of left side, find min of right side between a3, b3 and divide by 2 
        # always keep track of 4 variables
        # 2 from left side 2 from right side 
        # the 2 from left are endpoints of nums1 and nums2
        # the 2 from right sude are startpoints of nums1 and nums2

        # in case we need to take 0 elements of nums1 or nums2 on left side we assign the variable -inf in that case it is always smaller 
        # in case we need to have 0 elements of nums1 or nums2 on right side we assign the variable +inf cause then it will always be greater 

        # assuming nums1 smaller in size than nums 2 in the above algo 
        # cause want to run binary search on the smaller one so just resend to function nums2 as smaller

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = len(nums1)
        m = len(nums2)
        l, r = 0, n
        
        part = (n + m + 1) // 2
        
        while l <= r:
            mid = (l + r) // 2
            n1_left = mid # n1 elements on left side
            n2_left = part - mid # n2 elements on left side 
            
            # left waale
            x1 = float('-inf') if n1_left == 0 else nums1[n1_left - 1]
            x2 = float('-inf') if n2_left == 0 else nums2[n2_left - 1]
            # right waale
            x3 = float('inf') if n1_left == n else nums1[n1_left]
            x4 = float('inf') if n2_left == m else nums2[n2_left]
            
            if x1 <= x4 and x2 <= x3:
                if (n + m) % 2 != 0:
                    return max(x1, x2)
                else:
                    return (max(x1, x2) + min(x3, x4)) / 2
            elif x1 > x4:
                r = mid - 1
            else:
                l = mid + 1
        
        return 0

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        

        n = len(nums1)
        m = len(nums2)

        part_size = (n + m + 1) // 2
        l = 0
        r = n

        while l <= r: 
            mid = (l + r) // 2
            n1_left = mid 
            n2_left = part_size - mid

            # We are taking 0 elements on left side is the float condition for 
            a1 = float('-inf') if n1_left == 0 else nums1[n1_left - 1]
            b1 = float('-inf') if n2_left == 0 else nums2[n2_left - 1]

            # We took ALL elements of nums1 on the left side is the float condition for 
            a2 = float('inf') if n1_left == n else nums1[n1_left]
            b2 = float('inf') if n2_left == m else nums2[n2_left]

            # we have found the perfect partition
            if a1 <= b2 and b1 <= a2:
                # if odd number of numbers in final array then the median is just the middle value 
                if (n + m) % 2 != 0: 
                    return max(a1, b1)
                else:
                    return (max(a1, b1) + min(a2, b2)) / 2 
            
            # if we have not found the perfect partition
            elif a1 > b2: 
                # we need to move the right mpre to the left 
                r = mid - 1
            else: 
                # the value we 
                l = mid + 1
        return 0 

                