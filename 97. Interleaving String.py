#Starting from the end, using a 2d dp array 
#Check if we can have the current letter of s3 from either s1 or s2 and if we already had the previous letters then we get True
#Iteratively repeating the same process until we get to the first cell and it will have the final result
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for j in range(len(s1)+1)]

        dp[-1][-1] = True
        
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                elif j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]