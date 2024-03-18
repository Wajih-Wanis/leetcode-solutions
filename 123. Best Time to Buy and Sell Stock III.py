#The idea of this solution is to use dp to do a bottom up search for the maximum profits
#K here presents the maximum number of transactions allowed.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K = 2
        dp = [[[0 for _ in range(K + 1)] for _ in range(3)] for _ in range(len(prices) + 1)]
        
        for ind in range(len(prices) - 1, -1, -1):
            for b in range(2):
                for k in range(1, K + 1):
                    if b:
                        dp[ind][b][k] = max(-prices[ind] + dp[ind + 1][0][k], dp[ind + 1][b][k])
                    else:
                        dp[ind][b][k] = max(prices[ind] + dp[ind + 1][1][k - 1], dp[ind + 1][b][k])
        
        return dp[0][1][K]