class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last_fort_index = None
        max_captured = 0
        for i, num in enumerate(forts):
            if num in (1, -1):
                if last_fort_index is not None and forts[last_fort_index] * num == -1:
                    max_captured = max(max_captured, i - last_fort_index - 1)
                last_fort_index = i
        return max_captured
