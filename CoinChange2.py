# Leetcode Link: https://leetcode.com/problems/coin-change-ii/
# Category: DP or Dynamic Programming 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        We use a 2D table `t` where t[i][j] represents the number of ways to make amount `j` using the first `i` coins.

        Base Case:
        - There's exactly 1 way to make amount 0 (using no coins), so t[i][0] = 1 for all i.

        Transition:
        - If the current coin value is less than or equal to the current amount `j`,
          we add two cases:
            1. Including the coin: t[i][j - coin] (given in the question that we have an infinite number of coins)
            2. Excluding the coin: t[i-1][j]
        - Otherwise, we carry forward the previous value: t[i][j] = t[i-1][j]

        Time Complexity: O(n * amount)
        Space Complexity: O(n * amount)
        """
        n = len(coins)
        t = [[0 for j in range(amount + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            t[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    t[i][j] = t[i][j - coins[i - 1]] + t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]
        return t[n][amount]
