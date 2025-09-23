class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        O(N) solution would be to xor all elements a ^ a = 0 and the odd one out would be left when u xor the entire array. 

        O(log N) solution
        Think in terms of cases: 
        1. The current element == the next element
        to the right of the array, you have even number of elements
        example a [a b b]
        => the odd element will not be on the right side, move to the left array half

        to the right of the array, you have odd number of elements
        example a [a b b c]
        => the odd element has to be in this half cause you match and there are 3 elements left, obviously one would not be paired, so move to the right


        2. The current element != next element
        to the right of the array, you have even number of elements
        example a [b b c c]
        => the odd element cannot be here, move to the left
        to the right of the array, you have odd number of elements
        example a [b b c c d]
        the odd pairing can be here, move to the right
        '''
        l = 0
        n = len(nums)
        h = n - 1

        while (l < h):
            mid = l + (h - l)//2

            isEven = False
            if (h - mid) % 2 == 0:
                isEven = True
            

            if nums[mid + 1] == nums[mid]:
                if isEven:
                    l = mid + 2 # can skip the current 2 elements
                else:
                    h = mid - 1 
            else:
                # case wehre matching element could be to the left
                if isEven:
                    h = mid 
                else:
                    l = mid + 1
        return nums[h]
