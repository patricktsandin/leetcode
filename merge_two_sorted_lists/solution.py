class Solution:
    """Merges two sorted linked lists in O(n) time and O(1) space."""
    def mergeTwoLists(self, list1, list2):
        if not (list1 and list2):
            return list1 or list2 or None

        if list1.val < list2.val:
            list3_head = list3_tail = list1
            list1 = list1.next
        else:
            list3_head = list3_tail = list2
            list2 = list2.next

        while list1 and list2:
            if list1.val < list2.val:
                list3_tail.next = list1
                list3_tail = list3_tail.next
                list1 = list1.next
            else:
                list3_tail.next = list2
                list3_tail = list3_tail.next
                list2 = list2.next

        list3_tail.next = list1 or list2

        return list3_head
