class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        opMap = {}
        output = []
        A = list(A)
        length = len(A)

        for i, n in enumerate(A):
            if n in opMap:
                output.append(n)
            opMap[n] = i

        A.remove(output[0])
        expectedSum = length * (length + 1) // 2
        diff = expectedSum - sum(A)

        output.append(diff)
        return output
