class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        ctr = 0

        while ctr < len(nums):
            maxReach = max(maxReach, ctr+nums[ctr])
            if maxReach >= len(nums)-1:
                return True
            if maxReach == ctr:
                return False
            ctr += 1

        return False