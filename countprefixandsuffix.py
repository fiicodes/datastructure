class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for w in range(len(words)):
    
            for j in range(w+1, len(words)):
                if words[j].startswith(words[w]) and  words[j].endswith(words[w]):
                    count+=1
        return count






        
