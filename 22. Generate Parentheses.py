#We use two integer variables left & right to see how many '(' & ')' are in the current string
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(left, right, s):
            if len(s) == n*2:
                result.append(s)
                return 
            #If left < n then we can add '(' to the current string
            if left < n:
                dfs(left + 1, right, s + '(')
            #If right < left then we can add ')' to the current string
            if right < left:
                dfs(left, right + 1, s + ')')
                
        dfs(0, 0, '')
        return result