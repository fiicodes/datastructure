class Solution:
    def insert(self, arr):
        for i in range(1, len(arr)):
            curr = arr[i]
            j = i - 1
            while j >= 0 and curr < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = curr
        return arr


ob = Solution()
print(ob.insert([3, 56, 89, 9, 77, 12]))
