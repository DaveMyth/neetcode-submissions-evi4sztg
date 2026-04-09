class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        kv = {}

        ctr=0
        while(ctr<len(nums)):
            if((target-nums[ctr]) in kv and kv[target-nums[ctr]]!=ctr):
                return [kv[target-nums[ctr]], ctr]
            
            kv[nums[ctr]] = ctr
            ctr+=1

        return []
                