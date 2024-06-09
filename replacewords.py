class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)

        def find_shortest_root(word):
            prefix = ''
            for i, c in enumerate(word):

                prefix += c
                if prefix in dict_set:
                    return prefix
            return word

        res = []
        for word in sentence.split():
            shortest = find_shortest_root(word)
            res.append(shortest)
        return ' '.join(res)
