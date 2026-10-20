class Solution:
    # Time: O(n)
    # Space: O(n)
    def length_of_longest_substring(self, s: str) -> int:
        str_len = len(s)

        if str_len <= 1:
            return str_len

        htab = {c: 0 for c in s}
        total = len(htab.keys())

        return total