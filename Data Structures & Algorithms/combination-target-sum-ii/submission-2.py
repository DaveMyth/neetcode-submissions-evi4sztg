class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        print(candidates)

        def helper(currArr: List[int], currSum: int, currIdx: int) -> None:
            
            if currSum == target:
                res.append(currArr.copy())
                return

            if currIdx >= len(candidates) or currSum > target:
                return

            currArr.append(candidates[currIdx])
            helper(currArr, currSum + candidates[currIdx], currIdx + 1)
            currArr.pop()

            ctr = currIdx + 1
            while ctr < len(candidates) and candidates[currIdx] == candidates[ctr]:
                ctr+=1
            helper(currArr, currSum, ctr)

        helper([], 0, 0)

        return res