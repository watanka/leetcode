from itertools import permutations

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        length = len(words[0])
        num_words = len(words)

        answer = []

        for left in range(len(s) - length * num_words + 1) :
            start = left
            permutation = words.copy()
            
            while s[start : start + length] in permutation and permutation : # while sliding window word is in permutation
                try :
                    permutation.remove(s[start : start + length])
                except :
                    print(s[start : start + length])
                start += length
            if not permutation :
                answer.append(left)

            # print(permutation)



        return answer
                

            



