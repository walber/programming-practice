class Solution:
    # Time: O(n²)
    # Space: O(n)
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []

        k = 0
        lo = 1
        hi =  nums_len - 1
        
        while k < nums_len:
            offset = nums[k]

            while lo < hi and (nums[lo] <= 0 or nums[hi] >= 0):
                three_sum = nums[k] + nums[lo] + nums[hi]

                if three_sum == 0:
                    res.append([nums[k], nums[lo], nums[hi]])
                    prev_lo = nums[lo]
                    prev_hi = nums[hi]

                    while lo < hi and prev_lo == nums[lo]:
                        lo += 1
                        
                    while lo < hi and prev_hi == nums[hi]:
                        hi -= 1
                        
                elif three_sum > 0:
                    hi -= 1
                elif three_sum < 0:
                    lo += 1
            
            while k < nums_len and offset == nums[k]:
                k += 1                
            
            lo = k + 1
            hi = nums_len - 1
        
        return res