class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        #  Hello World
        # for letter in s :
        #     if letter != ' ' :
        #         substr = Hello -> ' '
        #         word_list.append(substr)
        #         substr = ''
        
        # ' fly me   to  the moon  '
        # fly -> word_list = ['fly']
        # me -> word_list = ['fly', 'me']
        # to -> word_list = ['fly', 'me', 'to']
        # the -> word_list = ['fly', 'me', 'to', 'the']
        # moon -> word_list = ['fly', 'me', 'to', 'the', 'moon']


        substr = ''
        word_list = []
        for letter in s :
            if letter != ' ' :
                substr += letter
            elif substr != '' and letter == ' ' : #
                word_list.append(substr)
                substr = ''
        # append remaining substr
        if substr :
            word_list.append(substr)

        # list의 마지막 원소 => word return
        return len(word_list[-1])

