class Solution:
    # Time: O(n²)
    # Space: O(1)
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            comp = target - n
            next_index = i + 1
            for j, m in enumerate(nums[next_index:], start=next_index):
                if m == comp:
                    return [i, j]
        
        return []