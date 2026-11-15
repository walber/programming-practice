class Solution:
    # Time: O(1)
    # Space: O(1)

    ROMAN_SYN = {
         'M': 1000,
        'CM': 900,
         'D': 500,
        'CD': 400,
         'C': 100,
        'XC': 90,
         'L': 50,
        'XL': 40,
         'X': 10,
        'IX': 9,
         'V': 5,
        'IV': 4,
         'I': 1
    }
    
    def roman_to_int(self, s: str) -> int:
        i = 0
        res = 0
        s_len = len(s)

        while s[i] == 'M':
            res += 1000
            i += 1

        while i < s_len:
            symbol = s[i:i + 2]
            
            if symbol in self.ROMAN_SYN:
                res += self.ROMAN_SYN[symbol]
                i += 1
            else:
                res += self.ROMAN_SYN[s[i]]
            
            i += 1

        return res