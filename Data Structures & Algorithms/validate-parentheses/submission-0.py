class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {"(": ")", "[": "]", "{": "}", "<": ">"}
        stack = []
        top = -1

        for ele in s:
            if ele in ["(" or "[" or "{" or "<"]:
                stack.append(ele)
                top += 1
            elif ele in [")" or "]" or "}" or ">"]:
                if top >= 0 and parantheses[stack[top]] == ele:
                    stack.pop()
                    top -= 1
                else:
                    stack.append(ele)
                    break
        if len(stack) == 0:
            return True
        else:
            return False