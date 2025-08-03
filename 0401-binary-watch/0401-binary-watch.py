class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        LEDS = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        n = len(LEDS)
        result = []
        def backtrack(index, hour, minute, lights_left):
            if index == n:
                if hour < 12 and minute < 60 and lights_left == 0:
                    result.append(f"{hour}:{minute:02d}")
                return
            if index < 4:
                hour += LEDS[index]
            else:
                minute += LEDS[index]
            backtrack(index + 1, hour, minute, lights_left - 1)
            if index < 4:
                hour -= LEDS[index]
            else:
                minute -= LEDS[index]
            backtrack(index + 1, hour, minute, lights_left)
        backtrack(0, 0, 0, turnedOn)
        return result