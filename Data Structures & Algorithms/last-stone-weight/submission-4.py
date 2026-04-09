class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            
            smashRes = -1 * abs(stone1 - stone2)
            if(smashRes < 0):
                heapq.heappush(stones, smashRes)

            print(stone1, stone2, smashRes)

        return abs(stones[0]) if len(stones) > 0 else 0