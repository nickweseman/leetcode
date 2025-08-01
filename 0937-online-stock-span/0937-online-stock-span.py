class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            p, span = self.stack.pop()
            count += span
        self.stack.append((price, count))
        return count