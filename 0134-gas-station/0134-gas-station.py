class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) :
            return -1

        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        total = 0
        res = 0
        for i in range(n) :
            total += diff[i]
            if total < 0 :
                res = i + 1
                total = 0
        return res