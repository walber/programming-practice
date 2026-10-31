class Solution:
    # Time: O(n)
    # Space: O(n)
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        res = []
        s_len = len(s)
        row_bound = num_rows - 1
        col_offset = 2 * row_bound
        num_cols = (s_len // num_rows) + 1
        
        for row in range(num_rows):
            for col in range(num_cols):
                c0 = col * col_offset
                c1 = c0 - row
                c2 = c0 + row

                # rows [1 .. n - 2]
                if 0 < row < row_bound:
                    if 0 <= c1 < s_len:
                        res.append(s[c1])

                if c2 < s_len:
                    res.append(s[c2])

        return "".join(res)