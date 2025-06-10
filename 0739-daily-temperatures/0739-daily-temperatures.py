class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                idx = stack.pop()
                result[idx] = i - idx 
            stack.append(i)
        return result