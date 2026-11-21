class Solution:
    # Time: O(3ⁿ)
    # Space: O(3ⁿ)

    PHONE_PAD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letter_combinations(self, digits: str) -> list[str]:        
        num_digits = len(digits)

        if num_digits == 0:
            return []

        num_elements = 1

        for d in digits:
            num_elements *= len(self.PHONE_PAD[d])
        
        buff = [[None] * num_digits for _ in range(num_elements)]

        for i in range(num_elements):
            r = i
            for j, d in enumerate(digits):
                chars = self.PHONE_PAD[d]
                chars_len = len(chars)

                p = r % chars_len
                r = r // chars_len
                buff[i][j] = chars[p] 

        res = map(lambda c : "".join(c), buff)
        return list(res)