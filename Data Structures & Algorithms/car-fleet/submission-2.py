class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        psPairs = [(position[ctr],speed[ctr]) for ctr in range(len(speed))]

        psPairs.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for pair in psPairs:
            t = (target-pair[0])/pair[1]

            if not stack or stack[-1] < t:
                stack.append(t)

        return len(stack)