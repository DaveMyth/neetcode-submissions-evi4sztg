class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0

        res = []
        while(r<len(nums)):
            if(r==l+k-1):
                res.append(max(nums[l:r+1]))
                l+=1
            r+=1

        return res