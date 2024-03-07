#Initalise an array with the size of the amount where each slot represents the minimum number of coins needed for that amount
#At the end if we are able to compose the amount with the available coins we return the slot at the index of the amount otherwise -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount +1)
        dp[0] = 0

        for a in range(1,amount+1):
            print(f"a = {a} dp = {dp}")
            for c in coins:
                print(f"dp[a] = {dp[a]} dp[a-c] = {dp[a-c]} coin is {c}")
                if a-c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)

        return dp[amount] if dp[amount] != amount+1 else -1
