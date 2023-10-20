class Solution:
    def reverseBits(self, n: int) -> int:
        string_binary = str(bin(n))[2:]
        string_binary = (32 - len(string_binary)) * '0' + string_binary

        return int('0b' + string_binary[::-1], 2)
        