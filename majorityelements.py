# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# --------------------------------solution-------------------------------------

#solution : 1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if res==n else -1)


        return res

#solution : 2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num] += 1

        n = n//2
        for key , value in m.items():
            if value > n:
                return key
        return None 

#solution : 3

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


        