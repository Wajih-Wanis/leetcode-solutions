from collections import List
"""
As this is my first ever problem on leetcode, I did it the first time using java and the solution was not optimal and it had a bad 
runtime and space usage. But now, as I am 128 problems in, I went back and did it again. 
The solution is really simple, just merging the two tables as if it was a mergeSort last step
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1.copy()
        temp = temp[:m]
        i = 0
        j = 0
        k = 0
        while k<m+n:
            if i>=m:
                nums1[k]=nums2[j]
                j+=1
            elif j<n and i<m and nums2[j] <= temp[i]:
                nums1[k]=nums2[j]
                j+=1
            else:
                nums1[k]=temp[i]
                i+=1
            k+=1