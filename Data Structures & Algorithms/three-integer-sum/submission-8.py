class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        def twoSum(start, end, target):
            startCpy = start
            while(start<end):
                if(start>startCpy and nums[start] == nums[start-1]):
                    start += 1
                    continue
                if(nums[start]+nums[end] == target):
                    res.append([-1*target, nums[start], nums[end]]) 
                    start += 1

                elif(nums[start]+nums[end]<target):
                    start += 1

                else:
                    end -= 1
        
        nums.sort()

        for idx, val in enumerate(nums):
            if(idx>0 and val==nums[idx-1]):
                continue

            twoSum(idx+1, len(nums)-1, -1*val)

        return res