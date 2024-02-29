#A sorted matrix -> A sorted array -> Binary search : That's how my brain saw it when I read the description. "w" 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = matrix[0]
        rows = len(matrix)
        for r in range(1,rows):
            flat.extend(matrix[r])
        def exists(array,target):
            size = len(array)
            if size == 1 :
                return array[0]==target
            middleValue = array[size//2]
            print(middleValue)
            if middleValue == target:
                return True
            elif middleValue > target:
                print(array)
                return exists(array[:size//2],target)
            else:
                return exists(array[size//2:],target)
        return exists(flat,target)
