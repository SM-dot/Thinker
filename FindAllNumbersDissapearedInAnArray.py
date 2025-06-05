# Leetcode link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Category: Arrays and HashMaps
# Optimal Solution O(1) space and O(n) time: 
# difficulty: medium 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
        In order to solve it using O(1) space, try using the nums space itself. If a number at index x in nums is marked as negative means that index + 1 it has been visited or exists in nums. If the value at index x in positive it means that that index + 1 has not been visited in nums. 


        How do u decide to make a number at index x negative?
        iterate through each element. nums[i], new index = nums[i-1]. Go to new index and mark the element negative. BUT NOTE: it is possible that the number is already negative, so if you again mark it as negative it will be +. Therefore u operate on absolute value. Similarly when findign new index, u do abs(nums[i]) - 1. 

        Note: if why we are doing -1, +1 for indexes and elements is confusing look at the question. The numbers are in range 1 -> n but indexes are in range 0 -> n -1. 
        Thus there is a clear mapping 
        number - 1 = index
        OR
        index + 1 = number

        This solution uses O(1) space and O(N) time. Now let's code!!!
        '''

        for num in nums:
            index = abs(num) - 1
            nums[index] = abs(nums[index]) * -1
        
        answer = []
        for i, n in enumerate(nums):
            if n > 0:
                answer.append(i+1)
        
        return answer 

# Time Complexity: O(N)
# Space Complexity: O(N)
# Difficulty: easy 

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bag = set()
        n = len(nums)

        for num in range(1, n + 1):
            bag.add(num)
        

        for num in nums:
            if num in bag:
                bag.remove(num)

        return list(bag) 