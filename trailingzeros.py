def count_trailing_zeroes(A):
    count = 0
    i = 5
    while A // i >= 1:
        count += A // i
        i *= 5
    return count
