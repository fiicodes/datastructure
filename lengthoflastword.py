import re



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
      w=s.split(" ")
      n=[]
      print(w)
      for i in w:
        if i != "":

           n.append(i)
      return(len(n[len(n)-1]))



o=Solution()
(o.lengthOfLastWord("   fly me   to   the moon  "))
