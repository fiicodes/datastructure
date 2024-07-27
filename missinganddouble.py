class Solution:
    def findTwoElement(self, arr, n):
        result = []
        hashmap = {}

        for num in arr:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        repeated = 0
        missing = 0

        for key, val in hashmap.items():
            if val == 2:
                repeated = key
                break


        for i in range(1, n + 1):
            if i not in hashmap:
                missing = i
                break

        result.append(repeated)
        result.append(missing)
        return result
