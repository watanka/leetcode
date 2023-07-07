class Solution:
    def minWindow(self, s : str, t: str) -> str :
        answer = ''

        # t에 있는 글자들과 갯수를 dictionary로 저장한다.
        tCount = {}
        for char in t :
            tCount[char] = tCount.get(char, 0) + 1
        
        # sCount에 substring에 채워야하는 글자들을 채워넣는다.
        sCount = {}
        for key, cnt in tCount.items() :
            sCount[key] = 0

        def test() :
            for key, val in tCount.items() :
                if val > sCount[key] :
                    return False
            return True

        left, right = 0, 0

        # 처음 보는 t 글자의 index로 left를 업데이트해준다.
        for i in range(len(s)) :
            if s[i] in sCount.keys() :
                left = i
                break
        
        for i in range(left, len(s)) :

            right = i
            if s[i] in tCount.keys() :
                sCount[s[i]] += 1
                while test() : # tCount의 값 중 하나라도 모자랄 경우, window substring 조건을 만족하지 못한 것
                    substring = s[left: right + 1]
                    if answer == '' or len(substring) < len(answer) :
                        answer = substring

                    # left 인덱스를 이동
                    sCount[s[left]] -= 1
                    for j in range(left+1, right+1) :
                        if s[j] in tCount.keys() :
                            left = j
                            break
        
        if test() :
            if answer == '' or len(substring) < len(answer) :
                answer = substring
        return answer


























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





