class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numset = set(nums)
        maxLen = 0

        for num in numset:
            if(num-1 in numset):
                continue

            ctr = 1
            currNum = num
            while(currNum+1 in numset):
                ctr += 1
                currNum += 1

            if(ctr>maxLen):
                maxLen = ctr

        return maxLen