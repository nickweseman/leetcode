class BrowserHistory:

    def __init__(self, homepage: str):
        self.fwd_stack = []
        self.bwd_stack = []
        self.current = homepage

    def visit(self, url: str) -> None:
        self.bwd_stack.append(self.current)
        self.current = url
        self.fwd_stack = []
    def back(self, steps: int) -> str:
        while steps > 0 and self.bwd_stack:
            self.fwd_stack.append(self.current)
            self.current = self.bwd_stack.pop()
            steps -= 1
        return self.current
    def forward(self, steps: int) -> str:
        while steps > 0 and self.fwd_stack:
            self.bwd_stack.append(self.current)
            self.current = self.fwd_stack.pop()
            steps -= 1
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)