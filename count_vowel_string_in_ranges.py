from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        prefix = [0] * (n+1)
        for i in range(n):
            word = words[i].lower()
            if word[0] in vowels and word[-1] in vowels:
                prefix[i +1] = prefix [i] +1
            else:
                prefix[i+1] = prefix[i]
        res = []
        for l, r in queries:
            res.append(prefix[r+1] - prefix [l])
        return res

