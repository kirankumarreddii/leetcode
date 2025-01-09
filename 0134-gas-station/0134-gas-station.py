class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        pos=0
        tot=0
        for i in range(len(cost)):
            tot+=(gas[i]-cost[i])
            if tot<0:
                tot=0
                pos=i+1
                
        return pos