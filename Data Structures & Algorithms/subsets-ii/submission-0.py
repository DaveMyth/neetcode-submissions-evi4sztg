class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def helper(currIdx: int, currArr: List[int]) -> None:

            if currIdx == len(nums):
                res.append(currArr.copy())
                return

            currArr.append(nums[currIdx])
            helper(currIdx+1, currArr)
            currArr.pop()

            currIdx += 1
            while currIdx < len(nums) and nums[currIdx] == nums[currIdx-1]:
                currIdx += 1
            helper(currIdx, currArr)
        
        helper(0, [])
        return res
        