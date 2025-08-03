class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = homepage
        self.bwd_stack = []
        self.fwd_stack = []
    def visit(self, url: str) -> None:
        self.fwd_stack = []
        self.bwd_stack.append(self.current)
        self.current = url
    def back(self, steps: int) -> str:
        while self.bwd_stack and steps > 0:
            self.fwd_stack.append(self.current)
            self.current = self.bwd_stack.pop()
            steps -= 1
        return self.current
    def forward(self, steps: int) -> str:
        while self.fwd_stack and steps > 0:
            self.bwd_stack.append(self.current)
            self.current = self.fwd_stack.pop()
            steps -= 1
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)