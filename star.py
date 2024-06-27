class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {}
        for i in edges:
            for j in i:
                if j not in hashmap:
                    hashmap[j] = 1
                else:
                    hashmap[j] += 1
        return next((key for key, count in hashmap.items() if count > 1), -1)

