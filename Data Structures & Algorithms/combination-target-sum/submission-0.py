class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(currSum: int, currIdx: int, currArr: List[int]) -> None:
            
            if currSum == target:
                res.append(currArr.copy())
                return

            if currSum > target or currIdx >= len(nums):
                return

            currArr.append(nums[currIdx])
            helper(currSum + nums[currIdx], currIdx, currArr)
            currArr.pop()

            helper(currSum, currIdx + 1, currArr)

        helper(0, 0, [])

        return res