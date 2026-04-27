class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        diff = [x-y for x,y in zip(gas, cost)]

        total = 0
        start = 0
        for idx, station in enumerate(diff):
            total += station
            if total < 0:
                total = 0
                start = idx+1
                continue

        return start