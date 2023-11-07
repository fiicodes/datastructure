class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        monsterArrivals = sorted([dist[i] / speed[i] for i in range(len(dist))])
        res = 0
        for i in range(len(monsterArrivals)):
            if i >= monsterArrivals[i]:
                return res
            res += 1
        return res
