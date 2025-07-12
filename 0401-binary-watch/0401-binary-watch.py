class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # first 4 are hours, next 6 are minutes
        LEDS = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        result = []

        def backtrack(start, leds_left, hour, minute):
            if hour > 11 or minute > 59: # 0-based values
                return
            
            if leds_left == 0:
                result.append(f"{hour}:{minute:02d}")
                return
            for i in range(start, len(LEDS)):
                if i < 4:
                    backtrack(i + 1, leds_left - 1, hour + LEDS[i], minute)
                else:
                    backtrack(i + 1, leds_left - 1, hour, minute + LEDS[i])
        backtrack(0, turnedOn, 0, 0)
        return result
