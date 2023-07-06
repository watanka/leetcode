class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = {}
        for word in words :
            count[word] = count.get(word, 0) + 1

        

        wordLength = len(words[0])
        
        answer = []

        for i in range(wordLength) :
            l = i
            currMap = {}

            for r in range(i, len(s) - wordLength + 1, wordLength) :
                word = s[r : r + wordLength]

                if word not in count :
                    currMap.clear()
                    l = r + wordLength

                else :
                    currMap[word] = currMap.get(word, 0) + 1
                    while currMap[word] > count[word] :
                        currMap[s[l : l + wordLength]] -= 1
                        l += wordLength
                    
                    if currMap == count :
                        answer.append(l)
        return answer

    