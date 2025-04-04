class Solution:
    def minCost(self, cost: List[List[int]]) -> int:
        
        for i in range(1,len(cost)):
            cost[i][0]+=min(cost[i-1][1],cost[i-1][2])
            cost[i][1]+=min(cost[i-1][2],cost[i-1][0])
            cost[i][2]+=min(cost[i-1][0],cost[i-1][1])
        return min(cost[-1])