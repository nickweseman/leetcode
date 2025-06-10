class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discounts = [0] * len(prices)
        stack = []

        for i, num in enumerate(prices):
            while stack and prices[stack[-1]] >= num:
                idx = stack.pop()
                discounts[idx] = num
            stack.append(i)
        return [prices[i] - discounts[i] for i in range(len(prices))]
        