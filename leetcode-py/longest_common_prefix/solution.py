class Solution:
    # Time: O(n * m)
    # Space: O(1)
    def longest_common_prefix(self, strs: list[str]) -> str:
        p_index = -1
        working = True
        common_prefix = ""
        longest_common_prefix = ""

        while working and p_index < len(strs[0]):
            common_prefix = strs[0][:p_index + 1]

            for word in strs:
                prefix = word[:p_index + 1]
                working = working and prefix == common_prefix

            if working:
                longest_common_prefix = common_prefix
                p_index += 1
        
        return longest_common_prefix