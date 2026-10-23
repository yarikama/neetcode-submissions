class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        num_of_zero_in_x = x.bit_length() - x.bit_count()
        n, x = list(bin(n)[2:]), list(bin(x)[2:])

        print(n, x)
        i, j = len(n)-1, len(x)-1

        while i >= 0 and j >= 0:
            if x[j] == "0":
                x[j] = n[i]
                i -= 1
            j -= 1

        x = n[:i+1] + x

        print(x)
        x = "".join(x)
        return int(x, 2)


