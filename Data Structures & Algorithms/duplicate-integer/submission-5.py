class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        newSet = set()
        for n in nums:
            if n in newSet:
                return True
            newSet.add(n)
        return False