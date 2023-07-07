from collections import defaultdict, Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        dict_t = Counter(t)
        needed = len(dict_t)
        found = 0
        l = 0
        result = float("inf"), None, None
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            if char in dict_t and window[char] == dict_t[char]:
                found += 1

            while l <= r and found == needed:
                char = s[l]

                if r - l + 1 < result[0]:
                    result = (r - l + 1, l, r)

                window[char] -= 1
                if char in dict_t and window[char] < dict_t[char]:
                    found -= 1
                
                l += 1
        
        length, l, r = result
        return "" if length == float("inf") else s[l:r+1]


        # ADOBECODEBANC ABC
        # dict_t = {A : 1, B: 2, C: 3}
        # needed = 3
        # found = 0
        # r : 0 l : 0 char: A window={A:1} found = 1  result (inf, 0, 0)
        # r : 1 l : 0 char: D window={A:1 D:1} found = 1  result (inf, 0, 0)
        # r : 2 l : 0 char: O window={A:1 D:1 O:1} found = 1  result (inf, 0, 0)
        # r : 3 l : 0 char: B window={A:1 D:1 O:1 B:1} found = 2  result (inf, 0, 0)
        # r : 4 l : 0 char: E window={A:1 D:1 O:1 B:1 E:1} found = 2  result (inf, 0, 0)
        # r : 5 l : 0 char: C window={A:1 D:1 O:1 B:1 E:1 C:1} found = 3  => char: A result (6, 0, 5) l : 1 found = 2
        # r : 6 l : 1 char: O window={A:0 D:1 O:2 B:1 E:1 C:1} found = 2 
        # r : 7 l : 1 char: D window={A:0 D:2 O:2 B:1 E:1 C:1} found = 2 
        # r : 8 l : 1 char: E window={A:0 D:2 O:2 B:1 E:2 C:1} found = 2 
        # r : 9 l : 1 char: B window={A:0 D:2 O:2 B:2 E:2 C:1} found = 2 
        # r : 10 l : 1 char: A window={A:1 D:2 O:2 B:2 E:2 C:1} found = 3 => char: C result (6, 5, 10) l : 6 found = 2
        # r : 11 l : 6 char: N window={A:1 D:1 O:1 B:1 E:1 C:0 N:1} found = 2
        # r : 12 l : 6 char: C window={A:1 D:1 O:1 B:1 E:1 C:1 N:1} found = 3 => char:O result(4, 9, 10) l : 10 found = 2




















    # def minWindow(self, s: str, t: str) -> str:
    #     def test(dic) :
    #         for v in dic.values() :
    #             if v > 0 :
    #                 return False
    #         return True

    #     if s == '' or t == '' : return ''

    #     count = {}
    #     for char in t :
    #         count[char] = count.get(char, 0) + 1

    #     m = len(s)
    #     n = len(t)
    #     minLength = m
        
    #     subString = ''

    #     for start in range(0, m - n + 1) :

    #         charMap = count.copy()
    #         end = start

    #         for r in range(end, min(end + minLength, m)) :
    #             if s[r] in charMap :
    #                 charMap[s[r]] -= 1
    #             # if find the match, it's the new minimum
    #             # print(charMap.values())
    #             if test(charMap) :
    #                 currLength = r - end
    #                 if currLength < minLength :
    #                     minLength = currLength
    #                     subString = s[start : r+1]

    #                 break
        
    #     return subString





