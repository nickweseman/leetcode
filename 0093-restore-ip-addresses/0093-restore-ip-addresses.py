class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        path = []
        result = []
        def backtrack(index):
            if index == n:
                if len(path) == 4:
                    result.append(".".join(path))
                return
            for i in range(index, n):
                segment = s[index : i + 1]
                
                if (0 <= int(segment) <= 255) and (len(segment) == 1 or (len(segment) > 1 and segment[0] != "0")):
                    path.append(segment)
                    backtrack(i + 1)
                    path.pop()
        backtrack(0)
        return result