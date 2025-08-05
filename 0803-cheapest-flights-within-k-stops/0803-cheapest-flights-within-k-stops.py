class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0
        for i in range(k + 1): # k + 1 because 2 nodes would be 1 stop
            temp_prices = prices.copy()
            for s, d, price in flights:
                if prices[s] == math.inf:
                    continue
                if prices[s] + price < temp_prices[d]:
                    temp_prices[d] = prices[s] + price
            prices = temp_prices
        return prices[dst] if prices[dst] != math.inf else -1

        