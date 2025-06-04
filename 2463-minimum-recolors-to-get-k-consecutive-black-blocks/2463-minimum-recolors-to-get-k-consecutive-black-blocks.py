from collections import defaultdict

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = right = 0
        window_whites = 0
        min_recolors = float('inf')

        while right < len(blocks):
            if blocks[right] == "W":
                window_whites += 1

            if right - left + 1 > k:
                if blocks[left] == "W":
                    window_whites -= 1
                left += 1
            
            if right - left + 1 == k:
                min_recolors = min(window_whites, min_recolors)
            right += 1
        return min_recolors
        