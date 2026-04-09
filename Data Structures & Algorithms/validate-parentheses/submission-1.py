class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracketMap = {')':'(', '}':'{', ']':'['}

        for c in s:
            if(c in bracketMap.values()):
                stack.append(c)
                continue
            if(stack and stack[-1] == bracketMap[c]):
                stack.pop()
                continue
            return False

        return not stack