class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer