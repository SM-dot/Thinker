# LeetCode Problem: Best Time to Buy and Sell Stock II
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Category: Arrays, Greedy Algorithms   

'''
Input: List of stock prices where prices[i] is the price of a given stock on day i
Operations:
- Iterate through the list of prices
- Keep track of the buy price
- If the current price is greater than the buy price, calculate the profit and update the buy price to the current price
- If the current price is less than the buy price, update the buy price to the current price
Output: Maximum profit that can be achieved by buying and selling the   stock multiple times
Time Complexity: O(n) where n is the number of days (length of prices)
Space Complexity: O(1) since we are using only a few variables to keep track of
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]

        for currPrice in prices:
            if buyPrice < currPrice:
                profit += currPrice - buyPrice
                buyPrice = currPrice
            elif currPrice < buyPrice:
                buyPrice = currPrice

        return profit 