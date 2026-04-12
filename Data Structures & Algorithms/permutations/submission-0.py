class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curArr: List[int], permutation: List[int]):

            if len(curArr) == 1:
                permutation.append(curArr[0])
                res.append(permutation)
                return
            
            for num in curArr:
                newArr = curArr.copy()
                newArr.remove(num)
                newPerm = permutation.copy()
                newPerm.append(num)
                helper(newArr, newPerm)

        helper(nums, [])
        return res