class Solution:
    # Time: O(n²)
    # Space: O(n²)
    def is_match(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len= len(p)
        dp_table = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]
        dp_table[0][0] = True

        for j, p_char in enumerate(p, 1):
            if j > 1 and p_char == '*':
                dp_table[0][j] = dp_table[0][j - 2]

        for i, s_char in enumerate(s, 1):
            for j, p_char in enumerate(p, 1):
                if p_char == '*':
                    if i > 1 and j > 1 and (s[i - 1] == s[i - 2] or p[j - 2] == '.'):
                        dp_table[i][j] = dp_table[i - 1][j]
                    
                    dp_table[i][j] = dp_table[i][j] or dp_table[i][j - 1]

                    if j > 1:
                        dp_table[i][j] = dp_table[i][j] or dp_table[i][j - 2]
                    
                elif p_char == s_char or p_char == '.':
                    dp_table[i][j] = dp_table[i - 1][j - 1]

        return dp_table[s_len][p_len]