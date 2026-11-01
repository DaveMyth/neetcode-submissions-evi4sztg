class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numCount = {}
        res = []
        freq = [[] for i in range(len(nums))]

        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)

        for num in numCount:
            freq[numCount[num]-1].append(num)

        ctr = len(nums)-1

        while ctr > -1 and k > 0:
            if len(freq[ctr]) == 0:
                ctr -= 1
                continue

            res.append(freq[ctr].pop())
            k -= 1

        return res