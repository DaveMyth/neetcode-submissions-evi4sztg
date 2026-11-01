class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        fix = 1
        for ctr in range(1,len(nums)):
            fix *= nums[ctr-1]
            res[ctr] *= fix

        fix = 1
        for ctr in range(len(nums)-2, -1, -1):
            fix *= nums[ctr+1]
            res[ctr] *= fix

        return res

