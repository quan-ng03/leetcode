import unittest
from easy.merge_two_sorted_list_21 import mergeTwoLists1, mergeTwoLists2, ListNode


def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


class TestMaxAchieveNum(unittest.TestCase):
    def test(self):
        list1 = list_to_linkedlist([1, 2, 4])
        list2 = list_to_linkedlist([1, 3, 4])

        merged1 = mergeTwoLists1(list1, list2)
        self.assertEqual(linkedlist_to_list(merged1), [1, 1, 2, 3, 4, 4])

        list1 = list_to_linkedlist([1, 2, 4])
        list2 = list_to_linkedlist([1, 3, 4])
        merged2 = mergeTwoLists2(list1, list2)
        self.assertEqual(linkedlist_to_list(merged2), [1, 1, 2, 3, 4, 4])


if __name__ == "__main__":
    unittest.main()
