class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # string에서 palidromic substring을 제거. 1회에 해당
        # s를 빈 string으로 만들기 위해 필요한 최소 횟수
        # s는 무조건 a, b로 이루어져있음

        # bbabaaabb
        # aba bbaabb 2
        # baaab bbab => bab b 3
        # aabbbbabab => abbbba
        
        return int(s == s[::-1]) or 2