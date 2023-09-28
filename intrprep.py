class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        for i in s:
            if i in hashmaps:
                hashmaps[i] += 1
            else:
                hashmaps[i] = 0

        for j in t:
            if j in hashmapt:
                hashmapt[j] += 1
            else:
                hashmapt[j] = 0
        return hashmaps == hashmapt


ob = Solution()
print(ob.isAnagram("abd", "ba"))
