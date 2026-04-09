class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums))]

        for num in nums:
            count[num] = 1 + count.get(num,0)

        for num in count:
            freq[count[num]-1].append(num)

        ctr=len(nums)-1
        res = []
        while(k>0 and ctr>-1):
            if(len(freq[ctr])==0):
                ctr-=1
                continue

            res.append(freq[ctr].pop(0))
            k-=1

        return res