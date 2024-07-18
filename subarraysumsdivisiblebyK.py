# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

#---------------------------------------solution-----------------------------------------


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        mapp = { 0:1 }

        for n in nums:
            currsum += n
            remain = currsum % k
            res += mapp.get(remain , 0)

            mapp[remain] = 1 + mapp.get(remain , 0)


        return res
        