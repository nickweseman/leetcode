class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i, num in enumerate(num):
            while stack and stack[-1] > num and k:
                stack.pop()
                k -= 1
            stack.append(num)

        if k:
            stack = stack[:-k]
        
        return "".join(stack).lstrip("0") or "0"
        