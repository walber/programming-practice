class Solution:
    # Time: O(n)
    # Space: O(n)

    PARENTHESES = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    def is_valid(self, s: str) -> bool:
        s_len = len(s)
        stack = []

        if s_len % 2 == 1:
            return False

        for p in s:
            if p in self.PARENTHESES:
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                
                c1 = stack.pop()
                c2 = self.PARENTHESES.get(c1, None)

                if p != c2:
                    return False

        return len(stack) == 0