class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total_shifts = 0
        for i in reversed(range(len(shifts))):
            total_shifts += shifts[i]
            shifts[i] = total_shifts
        
        ss = []
        for i, c in enumerate(s):
            start_pos = ord(c) - ord('a')
            end_pos = (start_pos + shifts[i]) % 26
            
            new_char = chr(end_pos + ord('a'))
            ss.append(new_char)
        return "".join(ss)