class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+*/-":
                el2 = stack.pop()
                el1 = stack.pop()
                
                if token == '+':
                    res = el1 + el2
                elif token == '-':
                    res = el1 - el2
                elif token == '/':
                    res = int(float(el1) / el2)
                else:
                    res = el1 * el2
                
                stack.append(res)
            else:
                stack.append(int(token))
        
        return stack[0]

