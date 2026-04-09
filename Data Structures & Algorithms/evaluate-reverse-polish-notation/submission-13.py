import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            print(stack)
            if not stack or token not in operators:
                stack.append(int(token))

            else:
                val2, val1 = stack.pop(), stack.pop()
                res = 0

                if(token == '+'):
                    res = val1 + val2
                elif(token == '-'):
                    res = val1 - val2
                elif(token == '*'):
                    res = val1 * val2
                elif(token == '/'):
                    res = val1 / val2
                    res = math.floor(res) if res > 0 else math.ceil(res)


                stack.append(res)

        return stack[0]
            