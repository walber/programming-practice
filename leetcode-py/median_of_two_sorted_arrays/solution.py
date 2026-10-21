class Solution:
    # Time: O(n)
    # Space: O(n)
    def find_median_sorted_arrays(self, nums1: list[int], nums2: list[int]) -> float:
        res = []
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0

        while i < n and j < m:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1 
            else:
                res.append(nums2[j])
                j += 1

        while i < n:
            res.append(nums1[i])
            i += 1

        while j < m:
            res.append(nums2[j])
            j += 1

        total_length = n + m
        half_index = total_length // 2
        
        if total_length & 1:
            return res[half_index]

        return (res[half_index] + res[half_index - 1]) / 2
