class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i]  = 1
            else:
                hashmap[i] +=1
        rev_char = sorted(hashmap.items(), key = lambda x:x[1], reverse= True)
        return  "".join([char*freq for char, freq in rev_char])