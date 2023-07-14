class Solution:
    def selection_sort(self, arr):
        for i in range(len(arr)):
            min = i
            for j in range(i + 1, len(arr)):
                if arr[min] > arr[j]:
                    min = j
            arr[min], arr[i] = arr[i], arr[min]
        return arr


obj = Solution()
print(obj.selection_sort([5, 7, 1, 3, 8]))
