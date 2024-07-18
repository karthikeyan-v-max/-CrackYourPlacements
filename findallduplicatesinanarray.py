# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

#-----------------------------------solution---------------------------------------


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            n = abs(n)
            
            if nums[n-2] < 0:
                res.append(n)

            nums[n-2] = -nums[n-2]


        return res
        