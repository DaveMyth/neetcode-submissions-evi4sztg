class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0]*len(temperatures)

        for ctr in range(len(temperatures)):
            while(stack and temperatures[ctr]>temperatures[stack[-1]]):
                res[stack[-1]] = ctr-stack[-1]
                stack.pop()
            stack.append(ctr)

        return res