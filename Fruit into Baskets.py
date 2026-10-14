# Leetcode: Fruit into Baskets
# Problem Link: https://leetcode.com/problems/fruit-into-baskets/
# Category: Sliding Window, Two Pointers, Hash Map

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        '''
        Brute force solution would be to go ahead and consider each starting point run the simulation and give the answer fo the best result but that would run in O(n sqaure time)

        We can do better, if u see closelt this is just a variation of longets substring with unique characters, here we have a few constraints. We cna only keep 2 numbers at max and when removing we only remove the one which is not the previos one.

        This would bring the complexity down to O(n) linear time from a square time. 

        Maybe we can do better and bring it down to O(1) but that can be seen. Now let's code.

        We should also note and keep the last occurence of the index of the two types that we are considering cause that is what would move the left and the right pointers and that is how we would measure the distance, cause it is possible that the earlier index gets removed and the occorence of the one we are trying to remove stays. 

        Can porbabbly do better with the space compexity here, instead of having a bag, we keep track of the last fruit index and the other fruit index 
        that would bring down the space complexity as well, but if we think about it then our bag is always of size 2, so it is not a big deal. hehehehehehehhe
        '''
        longestSubstring = 0
        bag = {}
        n = len(fruits)
        left = 0

        for right in range(n):
            if len(bag) < 2 or fruits[right] in bag:
                bag[fruits[right]] = right
                longestSubstring = max(longestSubstring, right - left + 1)
            else: 
                keepFruit = fruits[right - 1]
                for fruit in bag: 
                    if fruit != keepFruit: 
                        left = bag[fruit] + 1
                        del bag[fruit]
                        break
                bag[fruits[right]] = right
                longestSubstring = max(longestSubstring, right - left + 1)

        return longestSubstring 
                
