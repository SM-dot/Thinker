# LeetCode Problem: Majority Element
# LeetCode Link: https://leetcode.com/problems/majority-element/
# Category: Array, Divide and Conquer, Sorting, Counting
# Difficulty: Easy


# Method 1: OPTIMAL 
# # Explanation:
# # To find the majority element in an array, we can use the Boyer-Moore Voting Algorithm. The algorithm works by maintaining a count and a candidate for the majority element. We
# # iterate through the array, updating the candidate and count based on the current element. If
# # the count reaches zero, we select the current element as the new candidate. If the      
# # current element is the same as the candidate, we increment the count; otherwise, we
# # decrement the count. By the end of the iteration, the candidate will be the majority
# # element. This algorithm works because the majority element appears more than n/2 times,
# # ensuring that it will remain as the candidate by the end of the process.
# # Time Complexity: O(n), where n is the number of elements in the array,
# # Space Complexity: O(1), as we are using a constant amount of extra space.



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# Method 2:
# Explanation:
# To find the majority element in an array, we can use a hash map (dictionary) to count the occurrences of each element. We iterate through the array and for each element, we increment
# its count in the hash map. After populating the hash map, we iterate through its items to find the element with the maximum count, which will be our majority element. This approach
# works because the majority element appears more than n/2 times, ensuring that it will have
# the highest count in the hash map.
# Time Complexity: O(n), where n is the number of elements in the array, as
# we need to iterate through the array twice (once for counting and once for finding the maximum).
# Space Complexity: O(n), in the worst case, where all elements are unique and we need to store them in the hash map.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        answerVal = 0
        answer = -1

        for k, v in hm.items():
            if v > answerVal:
                answer = k
                answerVal = v
        
        return answer
