# 1865. Finding Pairs With a Certain Sum
# Problem Link: https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
# Category: Design, Hash Table, Two Pointers, Binary Search

'''
Explanation:
To solve the problem of finding pairs with a certain sum from two arrays, we can use a hash map to store the frequency of elements in the second array. This allows us to efficiently check how many times a complement (i.e., target sum minus an element from the first array) exists in
the second array.
When we need to add a value to an element in the second array, we update the hash
map accordingly. This ensures that our count operation remains efficient.
Time Complexity:
- Initialization: O(n) where n is the length of nums2 (to build the frequency
    map)
- Add operation: O(1) (updating the frequency map)
- Count operation: O(m) where m is the length of nums1 (iterating through nums1 to find pairs)
Space Complexity: O(n) for storing the frequency of elements in nums2
'''
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2Set = defaultdict(int)

        for num2 in nums2:
            self.nums2Set[num2] += 1

    def add(self, index: int, val: int) -> None:
        self.nums2Set[self.nums2[index]] -= 1
        self.nums2[index] += val 
        self.nums2Set[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1: 
            if tot - num in self.nums2Set:
                result += self.nums2Set[tot-num]
        return result 


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)