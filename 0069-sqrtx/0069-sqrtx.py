class Solution:
    def mySqrt(self, x: int) -> int:
        # input : 양의 정수
        # output : 제곱근 => 가장 가까운 양의 정수
        # built in 함수 사용하지 말 것.

        # ex1) 4 => 2
        # ex2) 8 => 2.8xx => 2 
        #   => 2**2 < 8 < 3**2

        # compare = 1 -> ++
        # if compare > x : return compare - 1
        # if compare == x : return compare

        # compare = 1 
        # while True :
        #     if compare ** 2 > x :
        #         return compare - 1
        #     elif compare ** 2 == x :
        #         return compare
        #     compare += 1 # instead of increasing by 1, we can increase more. 
        
        first, last = 1, x
        while first <= last :
            mid = first + (last - first) // 2
            if mid == x // mid :
                return mid
            elif mid > x // mid :
                last = mid - 1
            else :
                first = mid + 1
        return last



        # 1 2 3 4 5 6 7 8
        # 1 : [1 - 3] 3
        # 2 : [4 - 8] 5
        # 3 : [9 - 15] 7
        # ...



        