class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = altitude = 0

        for num in gain:
            altitude += num
            highest_altitude = max(highest_altitude, altitude)
        return highest_altitude