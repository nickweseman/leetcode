class Solution:
    def maxLength(self, arr: List[str]) -> int:
        trimmed_arr = []
        for word in arr:
            if len(word) == len(set(word)):
                trimmed_arr.append(word)
        max_length = 0
        chosen = set()
        n = len(trimmed_arr)
        def backtrack(index):
            nonlocal max_length
            if index == n:
                max_length = max(max_length, len(chosen))
                return
            my_set = set()
            for c in trimmed_arr[index]:
                my_set.add(c)
            if not (my_set & chosen):
                for c in trimmed_arr[index]:
                    chosen.add(c)
                backtrack(index + 1)
                for c in trimmed_arr[index]:
                    chosen.remove(c)
            backtrack(index + 1)
        backtrack(0)
        return max_length
