class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            altitude = [0] * (len(gain) + 1)  # Initialize the list with 0 values

            for i in range(1, len(altitude)):
                altitude[i] = altitude[i-1] + gain[i-1]

            return(max(altitude))








