class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        

        # k길이의 almost unique subarray들의 총합

        # almost unique subarray는 연속적인 subarry들 중 m개 이상의 unique한 값을 가질 경우
        seen = collections.defaultdict(int)

        summ = 0
        max_val = 0
        for idx, num in enumerate(nums) :
            summ += num
            seen[num] += 1
            if idx >= k :
                numsToRemove = nums[idx - k]
                summ -= numsToRemove
                seen[numsToRemove] -= 1
                if seen[numsToRemove] == 0 :
                    del seen[numsToRemove]
        
            if len(seen) >= m :
                max_val = max(summ, max_val)

        return max_val

