class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern)!=len(words):
            return False
        wordtochar={}
        chartoword={}
        for c,w in zip(pattern,words):
            if c in chartoword and chartoword[c]!=w:
                return False
            if w in wordtochar and wordtochar[w]!=c:
                return False
            chartoword[c]=w
            wordtochar[w]=c
        return True

#o(m+n) tc and space is also same

#below code for reducing space complexity

# class Solution:

#    def wordPattern(self, pattern, str):
#         strin = str.split(' ')
#         if len(pattern) != len(strin): return False
#         return len(set(zip(pattern, strin))) == len(set(strin)) and len(set(strin)) == len(set(pattern))

