# Leetcode 78. Subsets
# Problem Link: https://leetcode.com/problems/subsets/
# Category: Backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)

        '''
        Input: A list of integers nums
        Operations:
        - Use backtracking to generate all possible subsets of nums     
        - For each element, decide whether to include it in the current subset or not
        Output: A list of all subsets of nums
        T.C: O(2^N * N) where N is the number of elements in nums
        S.C: O(2^N * N) for storing all subsets,

        Explanation
        Time Complexity: 
        for each element 2 optios: take or dont take = 2^N

        Space Complexity: 
        total number of subsets = 2^N and for each of them we have their own list, in the worse case the length of the list is n thus S.C = O(2^N * N)
        
        Note: If there were duplicate elemnents our subsets would have dublicates, try a tree diagram with input [1, 2, 2] to see this
        '''

        def solve(i, subset):
            if i >= n:
                answer.append(subset[:])
                return 

            #not take case
            solve(i + 1, subset)

            #take case:
            subset.append(nums[i])
            solve(i + 1, subset)
            subset.pop()
            

        solve(0, [])
        return answer                 