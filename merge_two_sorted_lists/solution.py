from operator import attrgetter

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 or list2:
            return list1 or list2 or None

        list1_pointer = list1
        list2_pointer = list2
        list3_head = None
        list3_tail = None

        while True:
            if list1_pointer.val < list2_pointer.val:
                if not list3_head:
                    list3_head = list3_tail = list1_pointer
                else:
                    list3_tail.next = list1_pointer
                    list3_tail = list3_tail.next
                    list1_pointer = list1_pointer.next
                    list3_tail.next = None
            if list2_pointer.val < list1_pointer.val:
                if not list3_head:
                    list3_head = list3_tail = list2_pointer
                else:
                    list3_tail.next = list2_pointer
                    list3_tail = list3_tail.next
                    list2_pointer = list2_pointer.next
                    list3_tail.next = None
