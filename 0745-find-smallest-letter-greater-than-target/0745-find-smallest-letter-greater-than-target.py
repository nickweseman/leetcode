class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest_index, smallest_value = -1, math.inf

        for i, c in enumerate(letters):
            diff = ord(c) - ord(target)
            if 0 < diff < smallest_value:
                smallest_value = diff
                smallest_index = i
        return letters[0] if smallest_value == math.inf else letters[smallest_index]