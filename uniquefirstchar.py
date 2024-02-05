class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for i,v in  enumerate(s):
            if hashmap[v]==1:
                return i
        return -1

        