class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # needle_idx = 0
        # for i, hay in enumerate(haystack) :
        #     if hay == needle[needle_idx] :
        #         needle_idx += 1
        #         if needle_idx == len(needle) :
        #             return i - needle_idx + 1
        #     else :
        #         needle_idx = 0
        # return -1

        

        for i in range(len(haystack) - len(needle) + 1) :
            start_idx = 0
            while start_idx < len(needle) :
                if haystack[i + start_idx] == needle[start_idx] :
                    start_idx += 1
                else :
                    # 한글자라도 다를 경우 종료
                    break
            # 매칭 확인
            if start_idx == len(needle) :
                return i

        return -1