class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        # start from the last index as we want the greatest odd and its viable from the end of string
        while (i >= 0):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
            i -= 1
        return ''
