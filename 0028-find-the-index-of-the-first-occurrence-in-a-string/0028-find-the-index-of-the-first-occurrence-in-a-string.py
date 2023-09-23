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

        if len(haystack) == len(needle) :
            if haystack == needle :
                return 0
            else :
                return -1
            

        for i in range(len(haystack) - len(needle) + 1) :
            if haystack[i : i + len(needle)] == needle :
                return i
        return -1
