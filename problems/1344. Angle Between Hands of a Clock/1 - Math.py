class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(30 * hour + 0.5 * minutes - 6 * minutes)
        return min(angle, 360 - angle)
