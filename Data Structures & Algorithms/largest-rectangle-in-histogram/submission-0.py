class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        leftBdry = [-1]*n
        rightBdry = [n]*n

        stack = []

        for i in range(n):

            while(stack and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(stack):
                leftBdry[i] = stack[-1]

            stack.append(i)

        stack = []
        for j in range(n-1,-1,-1):

            while(stack and heights[stack[-1]]>=heights[j]):
                stack.pop()
            if(stack):
                rightBdry[j] = stack[-1] 

            stack.append(j)

        maxArea = 0

        for i in range(n):
            leftBdry[i] += 1
            rightBdry[i] -= 1

            maxArea = max(maxArea, (rightBdry[i]-leftBdry[i]+1)*heights[i])      
        return maxArea