class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in range(len(words)):
            for next_w in range(word+1,len(words)):
                if words[word] in words[next_w] and  words[word] not in res:
                    res.append(words[word])
                    break
                elif words[next_w] in words[word] and words[next_w] not in res:
                    res.append(words[next_w] )
        return res
            

