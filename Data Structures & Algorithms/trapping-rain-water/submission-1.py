class Solution:
    def trap(self, height: List[int]) -> int:
       
       lenH = len(height)
       leftWall, rightWall = [height[0]]*lenH, [height[-1]]*lenH

       ctr = 1
       while ctr<lenH:
            leftWall[ctr] = max(leftWall[ctr-1], height[ctr])
            rightWall[lenH-ctr-1] = max(rightWall[lenH-ctr], height[lenH-ctr-1])
            ctr += 1

       ctr = 0
       water = 0

       while ctr<lenH:
            water += min(leftWall[ctr], rightWall[ctr]) - height[ctr]
            ctr += 1

       return water