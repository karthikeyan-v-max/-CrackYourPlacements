# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# ----------------------solution-----------------------

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        h , l , m = len(nums)-1 , 0 , 0

        while m<=h:
            if nums[m] == 0:
                nums[l] , nums[m] = nums[m] , nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[h] , nums[m] = nums[m] , nums[h]
                h -= 1
            else:
                m += 1