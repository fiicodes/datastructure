class Solution:
    def rowWithMax1s(self, arr):
        row = len(arr)
        col = len(arr[0])

        global_an = 0
        index = -1
        for i in range(0, row):
            res = 0
            for j in range(0, col):

                if arr[i][j] == 1:
                    res += 1
            if res > global_an:
                global_an = res
                index = i

        return index
