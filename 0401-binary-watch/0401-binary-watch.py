class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        LEDS = [8,4,2,1,32,16,8,4,2,1]
        n = len(LEDS)
        def dfs(i, leds_left, hour, minute):
            if hour > 11 or minute > 59:
                return
            if leds_left == 0:
                result.append(f"{hour}:{minute:02d}")
                return
            if i == n:
                return
            if i < 4:
                dfs(i + 1, leds_left - 1, hour + LEDS[i], minute)
            else:
                dfs(i + 1, leds_left - 1, hour, minute + LEDS[i])
            dfs(i + 1, leds_left, hour, minute)
        dfs(0, turnedOn, 0, 0)
        return result