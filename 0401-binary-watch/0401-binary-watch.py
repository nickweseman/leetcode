class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        LEDS = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        result = []
        def backtrack(index, turned_on_left, hour, minute):
            if hour > 11 or minute > 59 or turned_on_left < 0:
                return
            if index == len(LEDS):
                if turned_on_left == 0:
                    result.append(f"{hour}:{minute:02d}")
                return
            if index < 4:
                backtrack(index + 1, turned_on_left - 1, hour + LEDS[index], minute)
            else:
                backtrack(index + 1, turned_on_left - 1, hour, minute + LEDS[index])
            backtrack(index + 1, turned_on_left, hour, minute)
        backtrack(0, turnedOn, 0, 0)
        return result
