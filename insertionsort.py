def insertionsort(arr):
    for i in range(1, len(arr)):
        curr_item = arr[i]
        j = i - 1
        while j >= 0 and curr_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_item


if __name__ == "__main__":
    arr = [3, 56, 89, 9, 77, 12]
    insertionsort(arr)
    print(arr)
