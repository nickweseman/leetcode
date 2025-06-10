class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        stack = []

        for i, num in enumerate(prices):
            while stack and prices[stack[-1]] >= num:
                result[stack.pop()] -= num
            stack.append(i)
        return result
        