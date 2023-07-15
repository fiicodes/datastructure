# array of N integers, indexed 0 to N-1;


# assume it’s populated with [1,4,2,-2,-9,10,2,12,2,-4,-4,-4,-4,2,6,7]
def peak(array):
    peak = array[0]
    N = len(array)
    index = 0
    output = []  # array of tuples
    for x in range(1, N - 1):
        if array[x] * array[x - 1] > 0:
            if peak < 0 and array[x] < peak:
                peak = array[x]
                index = x
            if peak >= 0 and array[x] > peak:
                peak = array[x]
                index = x

        else:
            output.append((index, peak))
            peak = array[x]
            index = x

    return output


print(peak([1, 4, 2, -2, -9, 10, 2, 12, 2, -4, -4, -4, -4, 2, 6, 7]))
