class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for ctr in range(len(temperatures)):

            while(stack and temperatures[stack[-1]] < temperatures[ctr]):
                idx = stack.pop()
                res[idx] = ctr - idx

            stack.append(ctr)

        return res