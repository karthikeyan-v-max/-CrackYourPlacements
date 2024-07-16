# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

#----------------------------------solution----------------------------------

1.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        if not nums:
            return nums
        
        while r<len(nums):
            while r < len(nums) and nums[l] == nums[r]:
                r = r + 1

            if r < len(nums) and nums[l] != nums[r]:
                nums[l+1] = nums[r]
                l += 1
                r += 1

        return l+1

2.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left+=1

        return left