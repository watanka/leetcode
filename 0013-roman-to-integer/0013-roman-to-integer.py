class Solution:
    def romanToInt(self, s: str) -> int :
        'III', 'LVIII', 'MCMXCIV'

        letter_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        result = 0
        s = s.replace('IV', '!')
        s = s.replace('IX', '@')
        s = s.replace('XL', '#')
        s = s.replace('XC', '$')
        s = s.replace('CD', '%')
        s = s.replace('CM', '^')

        for letter in s :
            if letter.isalpha() :
                # for 0 1 2 3 5 6 7 8
                result += letter_dict[letter]

            else :
                if letter == '!' :
                    result += 4
                elif letter == '@' :
                    result += 9
                elif letter == '#' :
                    result += 40
                elif letter == '$' :
                    result += 90
                elif letter == '%' :
                    result += 400
                elif letter == '^' :
                    result += 900
        return result
