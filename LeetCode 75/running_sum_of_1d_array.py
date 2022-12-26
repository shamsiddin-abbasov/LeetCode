# LeetCode 75 | Level 1 | Day 1 | 1

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] += nums[i]
        return nums
