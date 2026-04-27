class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        steps[n] = 1
        steps[n-1] = 1
        pos = n-2

        while pos > -1:
            steps[pos] = steps[pos+1] + steps[pos+2]
            pos-=1

        return steps[0]