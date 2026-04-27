class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ctr = 0
        l=r=0
        maxReach = 0

        while r<len(nums)-1:
            ctr += 1
            while l<=r:
                maxReach = max(l+nums[l], maxReach)
                l += 1
            l = r+1
            r = maxReach

        return ctr