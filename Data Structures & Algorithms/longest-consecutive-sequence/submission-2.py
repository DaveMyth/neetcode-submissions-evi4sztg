class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if num-1 in numSet:
                continue
            numCpy = num
            ctr = 1
            while numCpy+1 in numSet:
                ctr += 1
                numCpy += 1

            maxLen = max(ctr,maxLen)

        return maxLen