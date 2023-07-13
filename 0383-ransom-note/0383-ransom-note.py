class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # checked_letters = set()
        # for char in ransomNote :
        #     if char not in checked_letters and ransomNote.count(char) > magazine.count(char) :
        #         return False
        #     checked_letters.add(char)
        # return True

        
        
        
        
        
        
        # 2nd approach : get dictionary of magazine, and loop through ransomNote
        magazine_cnt = {}
        for char in magazine :
            magazine_cnt[char] = magazine_cnt.get(char, 0) + 1

        checked_letters = set()
        for char in ransomNote :
            if char in magazine_cnt :
                if char not in checked_letters :
                    if magazine_cnt[char] < ransomNote.count(char) :
                        return False


                # magazine_cnt[char] -= 1

                # if magazine_cnt[char] < 0 :
                #     return False
            else :
                return False
            checked_letters.add(char)

        return True
        
        
        
        
        
        # 1st approach : get dictionaries of both strings 
        # ransom_cnt = {}
        # for char in ransomNote :
        #     ransom_cnt[char] = ransom_cnt.get(char, 0) + 1

        # magazine_cnt = {}
        # for char in magazine :
        #     magazine_cnt[char] = magazine_cnt.get(char, 0) + 1

        # for char in ransom_cnt.keys() :
        #     if char in magazine_cnt :
        #         if magazine_cnt[char] < ransom_cnt[char] :
        #             return False
        #     else :
        #         return False
        # return True



        