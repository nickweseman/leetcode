class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]