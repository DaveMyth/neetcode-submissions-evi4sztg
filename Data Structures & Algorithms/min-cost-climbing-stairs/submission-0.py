class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        steps = [0] * (N+1)
        steps[N-1] = cost[N-1]

        ctr = N-2
        while ctr > -1:
            steps[ctr] = cost[ctr] + min(steps[ctr+1], steps[ctr+2])
            ctr -= 1

        return min(steps[0], steps[1])