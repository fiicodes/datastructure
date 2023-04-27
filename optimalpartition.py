class Solution:
    def partitionString(self, s: str) -> int:

         curset=set()
         res=1
         for c in s:
             if c in curset:
                 res+=1
                 curset=set()
             else:
                 curset.add(c)
         return res


            