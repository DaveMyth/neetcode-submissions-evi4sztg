class Solution:
    def trap(self, height: List[int]) -> int:
        lenH: int = len(height)
        leftWall: list[int] = [0]*lenH
        rightWall: list[int] = [0]*lenH

        leftWall[0] = height[0]
        rightWall[-1] = height[-1]

        for ctr in range(1,lenH):
            leftWall[ctr] = max(leftWall[ctr-1], height[ctr])
            rightWall[lenH-ctr-1] = max(rightWall[lenH-ctr], height[lenH-ctr-1])
        
        water = 0
        for ctr in range(0,lenH):
            # print(ctr, leftWall[ctr], rightWall[ctr])
            water += min(leftWall[ctr],rightWall[ctr])-height[ctr]
            print(water)

        return water