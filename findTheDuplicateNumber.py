# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.


# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

#----------------------------------solution-------------------------------------

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapp = {}

        for i in range(len(nums)):
            if nums[i] not in mapp:
                mapp[nums[i]] = i
            else:
                return nums[i]