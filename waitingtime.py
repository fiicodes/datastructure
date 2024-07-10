class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = 0
        time = 0
        n = (len(customers))

        for arrival, order in customers:
            if time > arrival:
                ans += time - arrival
            else:
                time = arrival
            ans += order
            time += order
        return ans / n






