class Solution:
    # Time: O(n)
    # Space: O(n)
    def length_of_longest_substring(self, s: str) -> int:
        str_len = len(s)

        if str_len <= 1:
            return str_len

        longest_len = 0
        substr_len = 0
        begin = 0
        htab = {}
        
        for i, c in enumerate(s):
            j = htab.get(c, -1)

            if j >= begin:
                begin = j + 1
                substr_len = i - begin
            
            htab[c] = i
            substr_len += 1
            longest_len = max(substr_len, longest_len)

        return longest_len