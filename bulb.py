class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulb=[1]*n
        for i in range(2,n):
            bulb[n]=0
        return bulb.count(1)
    