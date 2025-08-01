class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cleared_arr = []
        for word in arr:
            if len(word) == len(set(word)):
                cleared_arr.append(word)
        arr = cleared_arr
        chars = set()
        max_length = 0
        n = len(arr)
        def backtrack(index):
            nonlocal max_length
            if index == n:
                max_length = max(max_length, len(chars))
                return
            if len(set(arr[index]) & chars) == 0:
                for c in arr[index]:
                    chars.add(c)
                backtrack(index + 1)
                for c in arr[index]:
                    chars.remove(c)
            backtrack(index + 1)
        backtrack(0)
        return max_length