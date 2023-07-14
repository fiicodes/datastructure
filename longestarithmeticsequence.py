from collections import Counter


class Solution:
    def arithmeticsequence(arr):
        arr = sorted(arr)
        diff = []
        for i in range(0, len(arr) - 1):
            diff.append(arr[i + 1] - arr[i])
        for d in diff:
            counter = Counter(diff)
            most_common = counter.most_common(1)
            if most_common:
                d, counter = most_common[0]
                return counter + 1
            else:
                return 0


ob = Solution()
print(ob.longestArithSeqLength([3, 6, 9, 12]))
