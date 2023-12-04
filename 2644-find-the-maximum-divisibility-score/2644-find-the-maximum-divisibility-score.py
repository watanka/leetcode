class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxScore = 0
        answer = divisors[0]
        for divisor in divisors :
            divisible_cnt = 0
            for num in nums :
                if num % divisor == 0 :
                    divisible_cnt += 1
            if maxScore < divisible_cnt :    
                maxScore = max(maxScore, divisible_cnt)
                answer = divisor
            elif maxScore == divisible_cnt :
                answer = min(answer, divisor)

        return answer

