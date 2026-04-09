class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        minPace = float("inf")
        
        while(l<=r):
            mid = (l+r)//2
            timeTaken = 0
            for pile in piles:
                timeTaken += math.ceil(pile/mid)
            if(timeTaken <= h):
                r = mid-1
                minPace = min(minPace,mid)
            else:
                l = mid+1

        return minPace