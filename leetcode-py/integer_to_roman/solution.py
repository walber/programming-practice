class Solution:
    # Time: O(1)
    # Space: O(1)

    ROMAN_SYM = {
       1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
          9: 'IX',
          5: 'V',
          4: 'IV',
          1: 'I'
    } 
    
    def int_to_roman(self, num: int) -> str:
        symbols = []
        n = num // 1000
        res = num % 1000

        symbols.append('M' * n)

        for v in (100, 10, 1):
            n = res // v
            res = res % v

            if n == 9:
                symbols.append(self.ROMAN_SYM[9 * v])
            elif 5 <= n < 9:
                symbols.append(self.ROMAN_SYM[5 * v] + self.ROMAN_SYM[v] * (n % 5))
            elif n == 4:
                symbols.append(self.ROMAN_SYM[4 * v])
            else:
                symbols.append(self.ROMAN_SYM[v] * n)

        return "".join(symbols)