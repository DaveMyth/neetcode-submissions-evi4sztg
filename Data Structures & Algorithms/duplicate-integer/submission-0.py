class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        intSet = set()
        for num in nums:
            if(num in intSet):
                return True
            intSet.add(num)

        return False