class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxDict = {}
        
        for idx, val in enumerate(nums):
            req = target-val
            if(req in idxDict and idxDict[req] != idx):
                return [idxDict[req], idx]
            idxDict[val] = idx
        return []