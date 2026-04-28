# Leetcode:  Longest Mountain in Array
# Problem Link: https://leetcode.com/problems/longest-mountain-in-array/
# Category: Array, Two Pointers
# Difficulty: Medium


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        '''
        oK, a smart way to solve this would be to first go ahead and find the peaks in the arry. 
        Once you find the peaks, go ahead and from that peak move to the left and move to the right. see how far the pointers go, get that and then get the length of the mountain. 

        Once you have that simply compare it to the max that you have had so far. 

        This solution works in O(n) time and O(1) space cause u are not taking any extra space because of the pointer approach. Even though while and for loop

        ok, now lets code it up! 

        Time complexity: O(n) where n is the length of the input array arr. This is because we are iterating through the array once to find the peaks and then for each peak, we are moving the left and right pointers at most n times in total.
        Space complexity: O(1) because we are using only a constant amount of extra space
        '''
        n = len(arr)
        result = 0

        for i in range(1, n - 1):

            # check if we found a peak or not first 
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                left = i 
                right = i 

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                while right < n - 1 and arr[right + 1] < arr[right]:
                    right += 1
                
                currLength = right - left + 1 
                result = max(result, currLength)
        return result 
