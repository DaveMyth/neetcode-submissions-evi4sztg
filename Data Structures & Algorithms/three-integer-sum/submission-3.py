class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def twoSum(start: int, end: int, target: int) -> List[List[int]]:
            startCpy = start
            while(start<end):
                if(start>startCpy and nums[start] == nums[start-1]):
                    start+=1
                    continue
                currSum = nums[start] + nums[end]
                if(currSum == target):
                    self.res.append([nums[startCpy-1], nums[start], nums[end]])
                    start+=1
                elif(currSum<target):
                    start+=1
                else:
                    end-=1
        nums.sort()
        for idx, val in enumerate(nums):
            if(idx>0 and val == nums[idx-1]):
                continue
            
            twoSum(idx+1,len(nums)-1,-1*val)
        return self.res