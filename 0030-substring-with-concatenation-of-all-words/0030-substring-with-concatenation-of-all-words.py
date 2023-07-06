class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1
        
        lw = len(words[0])
        fin = []

        for i in range(lw):
            l = i
            window_hash = {}

            for r in range(i, len(s) - lw + 1, lw):
                word = s[r:r + lw]
                if word not in count:
                    window_hash.clear()
                    l = r + lw
                else:
                    window_hash[word] = window_hash.get(word, 0) + 1

                    while window_hash[word] > count[word]:
                        window_hash[s[l:l + lw]] -= 1
                        l += lw

                    if window_hash == count:
                        fin.append(l)

        return fin