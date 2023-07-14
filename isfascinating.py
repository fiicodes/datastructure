class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = 2 * n
        n3 = 3 * n
        n = str(n)
        hashmap = {}

        if len(n) == 3:
            n += str(n2)
            n += str(n3)
        for i in n:
            if i == "0":
                return False
            if i not in hashmap:
                hashmap[i] = 1
            else:
                return False
        return True


ob = Solution()
print(ob.isFascinating(192))
