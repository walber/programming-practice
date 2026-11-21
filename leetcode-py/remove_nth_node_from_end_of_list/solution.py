from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(n)
    def remove_nth_from_end(
        self, head: ListNode[int] | None, n: int
    ) -> ListNode[int] | None:

        node_list = []
        node = head
        i = 0 - n

        while node.next:
            node_list.append(node)
            node = node.next
            i += 1

        l1 = node_list[i - 1]
        l2 = node_list[i]
        l1.next = l2.next

        return head