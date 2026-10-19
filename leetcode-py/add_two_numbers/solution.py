from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def add_two_numbers(
        self, l1: ListNode[int] | None, l2: ListNode[int] | None
    ) -> ListNode[int] | None:
        output = []
        carryout = 0

        while l1 or l2:
            v = carryout
            
            if l1:
                v += l1.val
                l1 = l1.next

            if l2:
                v += l2.val
                l2 = l2.next

            output.append(v % 10)
            carryout = v // 10

        if carryout > 0:
            output.append(carryout)
        
        return ListNode.from_list(output)
