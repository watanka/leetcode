class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tank = 0
        base = 0
        i = 0

        while i < len(gas) :
            tank += gas[i] - cost[i]
            if tank < 0 :
                tank = 0
                base = i + 1
            i += 1

        i = 0
        while i < base :
            tank += gas[i] - cost[i]
            if tank < 0 : 
                return -1
            i += 1
        
        return base