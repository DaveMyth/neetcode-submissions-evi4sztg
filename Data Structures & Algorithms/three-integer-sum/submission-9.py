class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        def twoSum(start: int, end: int, target: int) -> None:

            startCpy = start
            while start<end:
                if (start > startCpy and nums[start] == nums[start-1]) or (target > nums[start]+nums[end]):
                    start += 1
                    continue

                elif (target < nums[start] + nums[end]):
                    end -= 1
                    continue

                else:
                    res.append([-1* target, nums[start], nums[end]])
                    start += 1

        nums.sort()
        ctr = 0
        while ctr < len(nums)-2:
            if ctr == 0 or nums[ctr] != nums[ctr-1]:
                twoSum(ctr+1, len(nums)-1, -1*nums[ctr])
            ctr += 1


        return res
