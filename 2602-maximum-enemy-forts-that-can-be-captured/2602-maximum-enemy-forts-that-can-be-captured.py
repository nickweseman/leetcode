class Solution:
    def captureForts(self, forts: List[int]) -> int:
        current_index = 0
        max_zeroes = 0
        last_fort_index = -1

        while current_index < len(forts):
            if forts[current_index] in (1, -1):
                if last_fort_index != -1 and forts[last_fort_index] * forts[current_index] == -1:
                    max_zeroes = max(max_zeroes, current_index - last_fort_index - 1)
                last_fort_index = current_index
            current_index += 1
        return max_zeroes