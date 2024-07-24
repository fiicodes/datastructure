def find_floor_and_ceiling(arr, x):
    arr.sort()  # Sort the array first

    floor = find_floor(arr, x)
    ceiling = find_ceiling(arr, x)

    return [floor, ceiling]


def find_floor(arr, x):
    left, right = 0, len(arr) - 1
    floor = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            floor = arr[mid]
            left = mid + 1
        else:
            right = mid - 1

    return floor


def find_ceiling(arr, x):
    left, right = 0, len(arr) - 1
    ceiling = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            ceiling = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return ceiling