class Solution:
    # Time: O(n²)
    # Space: O(1)
    def max_area(self, height: list[int]) -> int:
        best = 0

        for i, h1 in enumerate(height):
            for j, h2 in enumerate(height[i + 1:], i + 1):
                b = j - i
                h = min(h1, h2)
                best = max(best, h * b)

        return best