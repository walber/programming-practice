import math

class Solution:
    # Time: O(n)
    # Space: O(n)
    def convert(self, s: str, num_rows: int) -> str:
        res = []
        s_len = len(s)
        row_bound = num_rows - 1
        period = max(2 * row_bound, 1)
        num_cols = math.ceil(s_len / num_rows)
        
        for row in range(num_rows):
            for col in range(num_cols):
                c0 = col * period
                c1 = c0 - row
                c2 = c0 + row

                # rows [1 .. n - 2]
                if 0 < row < row_bound:
                    if 0 <= c1 < s_len:
                        res.append(s[c1])

                if c2 < s_len:
                    res.append(s[c2])

        return "".join(res)