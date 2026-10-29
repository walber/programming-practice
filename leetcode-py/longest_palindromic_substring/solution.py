class Solution:
    # Time: O(2) -> O(n) * 2 * O(n)
    # Space: O(1)
    def longest_palindrome(self, s: str) -> str:
        s_len = len(s)
        
        if s_len <= 2:
            return s if s[0] == s[-1] else s[0]

        best_l, best_r, best_len = 0, 0, 0

        for k in range(s_len):
            for c in (0, 1): 
                l = k
                r = k + c

                while l >= 0 and r < s_len and s[l] == s[r]:
                    p_len = r - l + 1
    
                    if p_len > best_len:
                        best_l = l
                        best_r = r
                        best_len = p_len
    
                    l -= 1
                    r += 1

        return s[best_l:best_r + 1]
            
