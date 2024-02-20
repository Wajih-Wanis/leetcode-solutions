class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,k):
            # Recursion will return False if (i,j) is out of bounds or board[i][j] != word[k] which is current letter we need
	        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or k >= len(word) or word[k] != board[i][j]:
		        return False

	        # If this statement is true then it means we have reach the last letter in the  word so we can return True
        	if k == len(word) - 1:
		        return True

        	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in directions:
		    # Since we can't use the same letter twice, I'm changing current board[i][j] to -1 before traversing further
        		tmp = board[i][j]
                board[i][j] = -1
		        # If dfs returns True then return True so there will be no further dfs
                if dfs(i + x, j + y, k + 1): 
			        return True
		        board[i][j] = tmp
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False