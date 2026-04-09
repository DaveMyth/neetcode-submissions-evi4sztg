class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def helper(idx: int) -> None:

            if idx >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            helper(idx+1)

            subset.pop()
            helper(idx+1)

        helper(0)
        return res