class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
       cost.append(0)#[10,15,20],0
       #here we add 0 at end to calculate math (out of bounce )
       for i in range(len(cost)-3,-1,-1):#here we need to start from 15 becz 20+0 is 20 so we need to start from len(cost)-3
            cost[i]+=min(cost[i+1],cost[i+2])
       return min(cost[0],cost[1])