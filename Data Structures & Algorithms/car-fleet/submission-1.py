class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []

        for pair in pairs:
            time = (target-pair[0])/pair[1]
            stack.append(time)

            if(len(stack)>1 and stack[-1]<=stack[-2]):
                stack.pop()
        return len(stack)