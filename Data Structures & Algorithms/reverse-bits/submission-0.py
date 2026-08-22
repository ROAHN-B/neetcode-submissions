class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_string=bin(n)[2:].zfill(32)[::-1]
        return int(reverse_string,2)