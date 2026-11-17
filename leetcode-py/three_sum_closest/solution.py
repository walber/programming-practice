class Solution:
    # Time: O(n²)
    # Space: O(1)
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)

        i = 1
        j = nums_len - 1

        offset = 0
        curr_sum = nums[0] + nums[1] + nums[2]
        best_sum = curr_sum
        
        while offset < nums_len:
            prev_offset = nums[offset]

            while i < j:
                curr_sum = nums[offset] + nums[i] + nums[j]
                s1 = abs(curr_sum - target)
                s2 = abs(best_sum - target)
                best_sum = curr_sum if s1 < s2 else best_sum

                if curr_sum > target:
                    j -= 1
                elif curr_sum < target:
                    i += 1
                else:
                    return curr_sum

            while offset < nums_len and prev_offset == nums[offset]:
                offset += 1

            i = offset + 1
            j = nums_len - 1

        return best_sum