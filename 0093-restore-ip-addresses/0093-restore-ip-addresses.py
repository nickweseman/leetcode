class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        result = []
        n = len(s)
        def backtrack(index):
            if index == n:
                if len(path) == 4:
                    result.append(".".join(path))
                return
            if len(path) == 4:
                return
            for i in range(index, n):
                substring = s[index: i + 1]
                if len(substring) > 1 and substring[0] == "0":
                    continue
                if not (0 <= int(substring) <= 255):
                    continue
                path.append(substring)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return result