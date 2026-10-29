class Solution:
    # Time: O(n)
    # Space: O(n)
    def my_atoi(self, s: str) -> int:
        ss = s.lstrip()
        read_len = len(ss)

        if read_len == 0:
            return 0

        is_negative = False
        valid_chars = []
        fst_char = ss[0]

        if fst_char.isalpha():
            return 0
        elif fst_char.isdigit():
            valid_chars.append(fst_char)
        elif fst_char == '-':
            is_negative = True

        for i in range(1, read_len):
            if ss[i] == '-' or ss[i] == '+':
                return 0
            elif ss[i].isdigit():
                valid_chars.append(ss[i])
            else:
                break

        if len(valid_chars) == 0:
            return 0
        
        j = 0
        while valid_chars[j] == '0':
            j += 1

        num = valid_chars[j:]

        if len(num) == 0:
            return 0

        int_read = int(''.join(num))
        max_int  = 2 ** 31
        
        if is_negative:
            return (max_int if int_read > max_int else int_read) * -1 
            
        return max_int - 1 if int_read >= max_int else int_read