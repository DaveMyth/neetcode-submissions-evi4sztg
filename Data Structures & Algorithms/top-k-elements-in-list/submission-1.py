class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ctrHash = {}
        res = []

        for num in nums:
            if(num in ctrHash):
                ctrHash[num] += 1
            else:
                ctrHash[num] = 1

        for key in sorted(ctrHash.keys(), key=lambda x: ctrHash[x], reverse=True):
            res.append(key)
            k-=1
            if(k==0):
                break

        return res
        