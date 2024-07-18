# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

#-------------------------------solution----------------------------


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapp = { 0:1 }
        res = 0
        cursumm = 0

        for n in nums:
            cursumm = cursumm + n

            diff = cursumm - k
            res += mapp.get(diff , 0)
            mapp[cursumm] = 1 + mapp.get(cursumm , 0)

        return res