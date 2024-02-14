"""
The intuition behind this solution is to get all the possible combinations possible thus a backtracking algorithm would be perfect
for this situation 
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = []
        digitChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i, seq):
            if i==lastLevel:
                result.append(seq)
                return
            for c in digitChar[digits[i]]:
                backtrack(i+1,seq+c)
        lastLevel = len(digits)
        i = 0
        backtrack(i,"")
        return result