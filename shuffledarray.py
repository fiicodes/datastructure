class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuf=[""]*(len(s))
        for i in range(len(s)):
            shuf[indices[i]]=s[i]
        return "".join(shuf)





       