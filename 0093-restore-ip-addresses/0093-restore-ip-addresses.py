class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        n = len(s)
        def backtrack(index):
            if index == n:
                if len(path) == 4:
                    result.append(".".join(path))
                return
            if len(path) == 4:
                return
            for length in range(1, 4): # explore lengths of 1, 2, or 3 characters
                # 1. Prevent creating a slice that goes out of bounds.
                if index + length > n:
                    break
                segment = s[index : index + length]
                if len(segment) > 1 and segment[0] == '0':
                    continue
                if not (0 <= int(segment) <= 255):
                    continue
                path.append(segment)
                backtrack(index + length)
                path.pop()
        backtrack(0)
        return result