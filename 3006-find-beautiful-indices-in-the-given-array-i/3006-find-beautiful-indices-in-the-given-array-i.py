class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        
        # find a and b

        def sliding(s, word):
            found = []
            for idx in range(len(s)-len(word)+1):
                if s[idx: idx + len(word)] == word:
                    found.append(idx)
            return found

        found_a = sliding(s, a)
        found_b = sliding(s, b)

        # k개 차이 이하의 a,b 조합 찾기
        answer = []
        for a in found_a:
            for b in found_b:
                if abs(a - b) <= k:
                    answer.append(a)
                    break
    
        return answer
                

        # bl = []
        # i = 0
        # while (i := s.find(a, i)) >= 0:
        #     j = i - k if i - k > 0 else 0
        #     if (j := s.find(b, j)) >= 0 and j - i <= k:
        #         bl.append(i)
        #     i += len(a)

        # return bl