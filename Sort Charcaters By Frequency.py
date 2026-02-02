# LeetCode Problem Link: https://leetcode.com/problems/sort-characters-by-frequency/
# LeetCode Problem: 451. Sort Characters By Frequency
# Category: Hash Table, String, Sorting, Heap Data Structure
# Difficulty: Medium

# Explanation: Could also be solved using bucket sort, in bucket sort instead of using an array use a map and then iterate with a for loop on the keys from back to front
# time complexity of the heap solution:
# Time Complexity: O(n log k), where n is the length of the string and k is the number of unique characters. Building the frequency map takes O(n) time, and pushing k elements into the heap takes O(k log k) time. Extracting elements from the heap takes O(n log k) time in total.
# Space Complexity: O(k), where k is the number of unique characters in the string, as we store the frequency of each character in the hash map and the heap.
# 
# Time complexity of bucket sort solution:
# Time Complexity: O(n), where n is the length of the string. Building the frequency map takes O(n) time, and constructing the result string takes O(n) time as well. 
class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap = defaultdict(int)

        for ch in s:
            freqMap[ch] += 1
        
        heap = []
        for ch, freq in freqMap.items():
            heapq.heappush(heap, (-freq, ch))
        
        answer = ""
        while heap: 
            count, char = heap[0]
            answer += char * -count
            heappop(heap)
        return answer 
        