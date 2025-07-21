class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.curr = 0
        path = []
        def backtrack(index):
            if index == len(characters):
                if len(path) == combinationLength:
                    self.combinations.append("".join(path))
                return
            path.append(characters[index])
            backtrack(index + 1)
            path.pop()
            backtrack(index + 1)
        backtrack(0)
    def next(self) -> str:
        s = self.combinations[self.curr]
        self.curr += 1
        return s
    def hasNext(self) -> bool:
        return self.curr < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()