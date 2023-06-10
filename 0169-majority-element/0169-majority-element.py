class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}

        for n in nums :
            if n not in cnt.keys() :
                cnt[n] = 1
            else :
                cnt[n] += 1

        return sorted(cnt.items(), key = lambda x : x[1], reverse = True)[0][0]