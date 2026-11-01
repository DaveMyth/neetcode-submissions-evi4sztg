class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        lenNums = len(nums)
        def twoSum(target, start, end):
            startCpy = start
            
            while start < end:
                if startCpy < start and nums[start] == nums[start-1]:
                    start += 1
                    continue

                currSum = nums[start] + nums[end]

                if currSum == target:
                    res.append([-1*target, nums[start], nums[end]])
                    start += 1

                elif currSum > target:
                    end -= 1

                else:
                    start += 1
        
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue
            # print(res)
            twoSum(-1*val, idx+1, lenNums-1)

        return res