class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        left = right = 0
        min_whites = float('inf')

        def window_valid() -> bool:
            return True
        
        def update_answer() -> None:
            nonlocal min_whites
            min_whites = min(min_whites, whites)

        while right < len(blocks):
            if blocks[right] == "W":
                whites += 1
            
            if right - left + 1 > k:
                if blocks[left] == "W":
                    whites -= 1
                left += 1
            
            if right - left + 1 == k and window_valid():
                update_answer()
            right += 1
        return min_whites