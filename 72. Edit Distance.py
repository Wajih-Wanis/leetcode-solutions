#Using a 2d matrix, we start from the backwards and make our way to the start of the matrix taking the minium number of changes everytime
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float(inf)] * (len(word2)+1) for i in range(len(word1)+1)]

        for i in range(len(word2)+1):
            dp[len(word1)][i] = len(word2)-i
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1)-i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j],dp[i][j+1], dp[i+1][j+1])


        return dp[0][0]

        