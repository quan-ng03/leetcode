import unittest
from medium.add_two_numbers_2 import addTwoNumbers, ListNode

# Helper function to convert a list into a linked list
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list back into a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

class TestaddTwoNumbers(unittest.TestCase):
    def test(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [7, 0, 8])

        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [0])

        l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = create_linked_list([9, 9, 9, 9])
        result = addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()
