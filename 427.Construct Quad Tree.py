"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
#The intuition of this solution is to simply go recursively through the matrix until we get all leafs, which is guaranteed because worst
#case scenario the leaf will be 1 cell and it will return. Thus we would divide the matrix into 4 sides and run them through, 
#Returning the result if they are leafs otherwise look for leafs inside them
class Solution:
    def makeTree(self,matrix):
        som = sum([sum(x) for x in matrix])
        n = len(matrix)
        if som==0 or som==n*n:
            return Node(som//(n*n),1,None,None,None,None)
        
        topMatrix = matrix[:n//2]
        botMatrix = matrix[n//2:]

        topLeft = list(map(lambda x:x[:n//2],topMatrix))
        topRight = list(map(lambda x:x[n//2:],topMatrix))
        botLeft = list(map(lambda x:x[:n//2],botMatrix))
        botRight = list(map(lambda x:x[n//2:],botMatrix))

        tl = self.makeTree(topLeft)
        tr = self.makeTree(topRight)
        bl = self.makeTree(botLeft)
        br = self.makeTree(botRight)

        return Node(1,0,tl,tr,bl,br)

    def construct(self, grid: List[List[int]]) -> 'Node':

        return self.makeTree(grid)
