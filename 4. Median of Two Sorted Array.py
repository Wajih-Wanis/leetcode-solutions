#The idea of this solution is to insert elements from two arrays in order as they are already sorted
#Once the temporary array reaches the size of half the sum of the input arrays
#We can safely assume that the last element is the median if the sum is odd 
#Otherwise if the sum is pair then the median is the average of the last element and the one before it
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums1Index = 0
        nums2Index = 0
        temp = []
        counter = 0
        while counter <= (m+n)//2:
            counter += 1
            #print(f"temp is {temp} and m is {m} and nums1Index is {nums1Index} and n is {n} and nums2Index is {nums2Index}")
            if nums1Index >= m and nums2Index < n:
                temp.append(nums2[nums2Index])
                nums2Index+=1
            elif nums2Index >= n and nums1Index < m:
                temp.append(nums1[nums1Index])
                nums1Index+=1
            if (nums1Index<m and nums2Index<n) and nums1[nums1Index]<=nums2[nums2Index]:
                temp.append(nums1[nums1Index])
                nums1Index += 1
            elif (nums1Index<m and nums2Index<n) and nums1[nums1Index]>nums2[nums2Index]:
                temp.append(nums2[nums2Index])
                nums2Index += 1
        return temp[-1] if (m+n)%2 else (temp[-1]+temp[-2])/2
