class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        
        i = 0 
        j = len(numbers) - 1
        while i < j :
            # 리스트의 중간값은 항상 처음과 마지막의 합이다
            output = numbers[i] + numbers[j]
            if output == target :
                return (i+1, j+1) # index값을 사람이 알아볼 수 있는 값으로 변환
            elif output < target :
                i += 1
            else :
                j -= 1

            

