class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        n = len(heights)
        leftBdry = [-1] * n
        rightBdry = [n] * n
        monStack = []

        for leftCtr in range(n):
            while monStack and heights[monStack[-1]] >= heights[leftCtr]:
                monStack.pop()

            if(monStack):
                leftBdry[leftCtr] = monStack[-1]
            monStack.append(leftCtr)

        monStack = []

        for rightCtr in range(n-1, -1, -1):
            while monStack and heights[monStack[-1]] >= heights[rightCtr]:
                monStack.pop()

            if(monStack):
                rightBdry[rightCtr] = monStack[-1]
            monStack.append(rightCtr)

        print(leftBdry, rightBdry)

        for ctr in range(n):
            area = (rightBdry[ctr] - leftBdry[ctr] -1) * heights[ctr]
            maxArea = max(maxArea, area)

        return maxArea