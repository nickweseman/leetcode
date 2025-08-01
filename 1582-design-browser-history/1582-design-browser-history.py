class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = []
        self.fwd_stack = []
        self.current = homepage
    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url
        self.fwd_stack = []
    def back(self, steps: int) -> str:
        while self.back_stack and steps > 0:
            self.fwd_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current
    def forward(self, steps: int) -> str:
        while self.fwd_stack and steps > 0:
            self.back_stack.append(self.current)
            self.current = self.fwd_stack.pop()
            steps -= 1
        return self.current
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)