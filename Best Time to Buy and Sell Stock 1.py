# LeetCode Problem: Best Time to Buy and Sell Stock I
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Category: Arrays, Greedy Algorithms

'''
Input: List of stock prices where prices[i] is the price of a given stock on day i
Operations:
- Iterate through the list of prices
- Keep track of the minimum price seen so far
- Calculate the profit if the stock were sold on the current day
- Update the maximum profit if the current profit is greater than the previously recorded maximum profit
Output: Maximum profit that can be achieved by buying and selling the stock once
Time Complexity: O(n) where n is the number of days (length of prices)
Space Complexity: O(1) since we are using only a few variables to keep track of
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0

        for currPrice in prices:
            if currPrice < buyPrice: 
                buyPrice = currPrice
            elif currPrice > buyPrice: 
                profit = max(profit, currPrice - buyPrice)
        
        return profit 
