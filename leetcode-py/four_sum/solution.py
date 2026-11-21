class Solution:
    # Time: O(n³)
    # Space: O(n)
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()

        nums_len = len(nums)

        if nums_len < 4:
            return []

        i = 0
        res = []

        while i < nums_len - 3:
            j = i + 1
            prev_i = i
            
            while j < nums_len - 2:
                k = j + 1
                prev_j = j
                m = nums_len - 1

                while k < m:
                    prev_k = k
                    curr_sum = nums[i] + nums[j] + nums[k] + nums[m]
        
                    if curr_sum > target:
                        m -= 1
                    elif curr_sum < target:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[m]])
                        
                        while k < m and nums[k] == nums[prev_k]:
                            k += 1

                while j < nums_len - 2 and nums[j] == nums[prev_j]:
                    j += 1

            while i < nums_len - 3 and nums[i] == nums[prev_i]:
                i += 1 

        return res