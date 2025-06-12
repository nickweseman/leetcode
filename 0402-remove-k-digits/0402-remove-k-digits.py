class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i, digit in enumerate(num):
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        if k > 0:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"