class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_cnt = {}
        for char in ransomNote :
            ransom_cnt[char] = ransom_cnt.get(char, 0) + 1

        magazine_cnt = {}
        for char in magazine :
            magazine_cnt[char] = magazine_cnt.get(char, 0) + 1

        for char in ransom_cnt.keys() :
            if char in magazine_cnt :
                if magazine_cnt[char] < ransom_cnt[char] :
                    return False
            else :
                return False
        return True



        