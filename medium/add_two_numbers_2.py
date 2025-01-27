
"""
    Lowkey hardcoded this.
    1. Convert the linked list to integer
    2. Add them, convert the sum to string and reverse it, then convert it to list
    3. Create a new linked list and add the elements from the list to the linked list
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    mult = 1
    i1 = 0
    i2 = 0
    result = ListNode()
    current = result

    while l1:
        i1 += l1.val * mult
        mult *= 10
        l1 = l1.next
    mult = 1
    while l2:
        i2 += l2.val * mult
        mult *= 10
        l2 = l2.next
    sum = i1 + i2
    inv_sum = str(sum)[::-1]
    st = [int(i) for i in inv_sum]
    for i in st:
        current.next = ListNode(i)
        current = current.next
    return result.next




    
    