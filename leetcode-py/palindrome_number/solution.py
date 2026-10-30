class Solution:
    # Time: O(n)
    # Space: O(n)
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x > 0 and x % 10 == 0:
            return False

        res = [x % 10]
        n = x // 10
        
        while n > 0:
            res.append(n % 10)
            n = n // 10

        i = 0
        j = len(res) - 1

        while i <= j:
            if res[i] != res[j]:
                return False

            i += 1
            j -= 1
            
        return True