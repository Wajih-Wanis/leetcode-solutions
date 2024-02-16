"""
The first thing that came to my mind when reading the description is that the algorithm should be a tree like algorithm with all the
possible words thus I thought of the Trie algorithm.
"""
from collections import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self,word):
        cur = self
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board),len(board[0])
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        visited, res = set(),set()
        def dfs(word,node,r,c):
            if (r<0 or c<0 or r==m or c==n or not(board[r][c]  in node.children) or (r,c) in visited):
                return 
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for i,j in directions:
                dfs(word, node, r+i,c+j)
            visited.remove((r,c))

        for i in range(m):
            for j in range(n):
                dfs("",root,i,j)

        return list(res)