class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.curr = 0
        self.combinations = []
        comb = []
        def dfs(i):
            if len(comb) == combinationLength:
                self.combinations.append("".join(comb))
                return
            if i == len(characters):
                return
            comb.append(characters[i])
            dfs(i + 1)
            comb.pop()
            dfs(i + 1)
        dfs(0)
    def next(self) -> str:
        result = self.combinations[self.curr]
        self.curr += 1
        return result
    def hasNext(self) -> bool:
        return self.curr < len(self.combinations)