class Solution:
    # Time: O(n²)
    # Space: O(n)
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []
        k = 0
        
        while k < nums_len:
            prev_k = k
            lo = k + 1
            hi = nums_len - 1

            while lo < hi and (nums[lo] <= 0 or nums[hi] >= 0):
                three_sum = nums[k] + nums[lo] + nums[hi]

                if three_sum > 0:
                    hi -= 1
                elif three_sum < 0:
                    lo += 1
                else:
                    res.append([nums[k], nums[lo], nums[hi]])
                    prev_lo = lo
                    prev_hi = hi

                    while lo < hi and nums[lo] == nums[prev_lo]:
                        lo += 1
                        
                    while lo < hi and nums[hi] == nums[prev_hi]:
                        hi -= 1

            while k < nums_len and nums[k] == nums[prev_k]:
                k += 1

        return res