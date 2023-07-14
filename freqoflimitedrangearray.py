class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.

    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, P, N):
        hashmap = {}
        for i in range(1, P + 1):
            hashmap[i] = 0
        for num in arr:
            if num <= P:
                hashmap[num] += 1
        return hashmap.values()


ob = Solution()
print(ob.frequencyCount([2, 3, 2, 3, 5], 5, 5))
