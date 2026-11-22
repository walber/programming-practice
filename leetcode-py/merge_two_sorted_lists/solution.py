from leetcode_py import ListNode


class Solution:
    # Time: O(n)
    # Space: O(1)
    def merge_two_lists(
        self, list1: ListNode[int] | None, list2: ListNode[int] | None
    ) -> ListNode[int] | None:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        l1 = list1
        l2 = list2
        head = None
        merger = None

        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        merger = head

        while l1 and l2:
            if l1.val <= l2.val:
                merger.next = l1
                l1 = l1.next
            else:
                merger.next = l2
                l2 = l2.next

            merger = merger.next

        if l1:
            merger.next = l1
        elif l2:
            merger.next = l2

        return head