class Solution:
    # Time: O(n)
    # Space: O(1)
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        if len(nums) <= 1:
            return []
        
        complement = target - nums[0]
        complement_dict = {complement: 0}

        for j, n in enumerate(nums[1:], start=1):
            complement = target - n
            i = complement_dict.get(n)

            if i is not None:
                return [i, j]
                
            complement_dict[complement] = j
        
        return []