class Solution:
    def captureForts(self, forts: List[int]) -> int:
        last_fort_index = 0
        max_forts = 0

        for fort_index, fort_value in enumerate(forts):
            if fort_value != 0:
                if forts[last_fort_index] * fort_value == -1:
                    max_forts = max(max_forts, fort_index - last_fort_index - 1)
                last_fort_index = fort_index
        return max_forts