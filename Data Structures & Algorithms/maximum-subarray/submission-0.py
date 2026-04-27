class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=r=1
        currSum = nums[0]
        maxSum = nums[0]

        while r<len(nums):
            if currSum < 0:
                l = r
                currSum = 0
            
            currSum += nums[r]
            maxSum = max(currSum, maxSum)
            r += 1

        return maxSum