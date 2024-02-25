from collections import List
"""
The idea of this solution is to iterate once through the table and calculating the sum while getting rid of any negative prefix value.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        prefix = 0
        for d in nums:
            if prefix < 0:
                prefix = 0
            prefix += d
            result = max(result,prefix)
        return result