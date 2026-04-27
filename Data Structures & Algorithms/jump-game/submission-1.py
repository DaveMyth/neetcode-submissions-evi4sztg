class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        ctr = 0

        while ctr <= maxReach:
            maxReach = max(maxReach, ctr+nums[ctr])
            if maxReach >= len(nums)-1:
                return True
            
            ctr += 1
        return False