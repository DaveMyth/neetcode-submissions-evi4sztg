class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        minK = float("inf")

        while (l<=r):
            mid = (l + r) // 2

            currTime = 0
            for pile in piles:
                currTime += math.ceil(pile/mid)
            
            if(currTime <= h):
                if minK > mid:
                    minK = mid
                r = mid - 1
            else:
                l = mid + 1

        return minK