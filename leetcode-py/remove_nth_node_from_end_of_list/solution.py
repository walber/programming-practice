from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def remove_nth_from_end(
        self, head: ListNode[int] | None, n: int
    ) -> ListNode[int] | None:

        node_list = [None] * (n + 1)
        node = head

        while node:
            node_list.pop(0)
            node_list.append(node)
            node = node.next

        l1 = node_list[0]
        l2 = node_list[1]

        if l1 is None:
            head = l2.next
        else:
            l1.next = l2.next

        return head