class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif bool(stack):
                char = stack[-1]
                if char == '(' and c == ')':
                    stack.pop()
                elif char == '{' and c == '}':
                    stack.pop()
                elif char == '[' and c == ']':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)


        return not bool(stack)
        