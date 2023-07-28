def mergeSort(arr: [int]):
    # Write Your Code Here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    leftarray = arr[:mid]
    rightarray = arr[mid:]
    leftarray = mergeSort(leftarray)
    rightarray = mergeSort(rightarray)
    return merge(leftarray, rightarray)


def merge(l, r):
    merged = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(l) and rightindex < len(r):
        if l[leftindex] < r[rightindex]:
            merged.append(l[leftindex])
            leftindex += 1
        else:
            merged.append(r[rightindex])
            rightindex += 1
    merged.extend(l[leftindex:])
    merged.extend(r[rightindex:])
    return merged


print(mergeSort([3, 67, 88, 52, 5, 12, 40]))
