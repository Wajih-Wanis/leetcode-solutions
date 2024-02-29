#In the last solution for this problem it took O(n) to flatten the matrix, and O(log(m*n)) to perform the binary search on the flat list. However, it was not that optimal as it only did better than 44% of the solution.
#In this solution it takes O(m) to find which row ( if it exists ) contains the target. Once the row is found (if no row found returns false) then it performs binary search on that row alone which takes O(log(n)) and thus this solution performer better than 92% than other solutions.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        container = []
        for row in matrix:
            if target==row[0] or target == row[-1]:
                return True
            elif row[0] < target < row[-1]:
                container = row
                break
        if container == []:
            return False
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
        return exists(container,target)

