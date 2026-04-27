class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        cache = [0] * (N + 1)
        cache[N-1] = nums[N-1]

        ctr = N-2
        while ctr > -1:
            cache[ctr] = max(nums[ctr] + cache[ctr+2], cache[ctr+1])
            ctr -= 1

        return cache[0]