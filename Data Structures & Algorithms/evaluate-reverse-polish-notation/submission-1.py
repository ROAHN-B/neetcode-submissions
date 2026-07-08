class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ele in tokens:
            if ele.isdigit():
                stack.append(int(ele))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if ele == "+":
                    stack.append(int(num1 + num2))
                elif ele == "-":
                    stack.append(int(num1 - num2))
                elif ele == "/":
                    stack.append(int(num1 / num2))
                elif ele == "*":
                    stack.append(int(num1 * num2))
        return stack[0]
