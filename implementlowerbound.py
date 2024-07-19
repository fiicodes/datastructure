def findFloor(self, A, N, X):
    if X == 0:
        return -1
    ans = -1
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] <= X:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


