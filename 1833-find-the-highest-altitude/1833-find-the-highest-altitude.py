class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = highest_altitude = 0

        for i, num in enumerate(gain):
            altitude += num
            highest_altitude = max(highest_altitude, altitude)
        return highest_altitude