class Solution:
    # Time: O(logn)
    # Space: O(1)
    def reverse(self, x: int) -> int:
        n, m, max_int = abs(x), 0, 2 ** 31

        while n > 0:
            m = m * 10 + (n % 10)
            n = n // 10

        if x >= 0 and m < max_int - 1:
            return m

        if x < 0:
            if m <= max_int:
                return m * -1
        else:
            if m < max_int:
                return m
        
        return 0