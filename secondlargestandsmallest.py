def getSecondOrderElements(n: int, a: [int]) -> [int]:
    sorted_min = sorted(a)
    res = []
    res.append(sorted_min[n - 2])
    res.append(sorted_min[1])
    return res


print(getSecondOrderElements(5, [1, 2, 3, 4, 5]))


# Write your code here.
