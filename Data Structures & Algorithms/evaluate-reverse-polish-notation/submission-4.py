import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = ['+','-','*','/']

        for c in tokens:
            print(stack)
            if(c not in operators):
                stack.append(int(c))
                continue
            b = stack.pop()
            a = stack.pop()

            res = 0
            if(c == operators[0]):
                stack.append(a+b)
            elif(c == operators[1]):
                stack.append(a-b)
            elif(c == operators[2]):
                stack.append(a*b)
            else:
                res = a/b
                stack.append(math.floor(res) if res>0 else math.ceil(res))

        return stack[0] 