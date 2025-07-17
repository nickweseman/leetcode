class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique_arr = []
        for s in arr:
            if len(set(s)) == len(s):
                unique_arr.append(s)
        chars = set()
        max_length = 0
        def backtrack(index):
            nonlocal max_length
            if index == len(unique_arr):
                max_length = max(max_length, len(chars))
                return
            if not (set(unique_arr[index]) & chars):
                for c in unique_arr[index]:
                    chars.add(c)
                backtrack(index + 1)
                for c in unique_arr[index]:
                    chars.remove(c)
            backtrack(index + 1)
        backtrack(0)
        return max_length