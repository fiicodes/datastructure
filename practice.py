class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")

        s=[c for c in s if c!=""]
        print(s)

        return len(s[-1])


ob=Solution()
print(ob.lengthOfLastWord("   fly me   to   the moon  "))