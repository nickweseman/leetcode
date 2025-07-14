class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique_arr = []
        for s in arr:
            if len(set(s)) == len(s):
                unique_arr.append(s)
        comb_char_set = set()
        max_length = -math.inf
        def dfs(i):
            nonlocal max_length
            if i == len(unique_arr):
                max_length = max(max_length, len(comb_char_set))
                return
            if not set(unique_arr[i]).intersection(comb_char_set):
                for char in unique_arr[i]:
                    comb_char_set.add(char)
                dfs(i + 1)
                for char in unique_arr[i]:
                    comb_char_set.remove(char)
            dfs(i + 1)
        dfs(0)
        return max_length