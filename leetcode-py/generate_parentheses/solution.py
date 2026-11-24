class Solution:
    # Time: O(4ⁿ * n)
    # Space: O(n)
    def generate_parenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack(n_opened: int, n_closed: int):
            if n_opened == n_closed == n:
                res.append("".join(stack))
            else:
                if n_opened < n:
                    stack.append('(')
                    backtrack(n_opened + 1, n_closed)
                    stack.pop()
                    
                if n_closed < n_opened:
                    stack.append(')')
                    backtrack(n_opened, n_closed + 1)
                    stack.pop()

        backtrack(0, 0)
        return res