# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists1(list1, list2):
    
    # This is the brute force method of merging two lists
    arr = []
    
    # Convert linked lists to arrays
    while list1:
        arr.append(list1.val)
        list1 = list1.next
    while list2:
        arr.append(list2.val)
        list2 = list2.next
    # Sort the list
    arr.sort()
    
    # Convert the sorted array back to a linked list
    result = ListNode()
    curr = result
    for value in arr:
        curr.next = ListNode(value)
        curr = curr.next
    return result.next

def mergeTwoLists2(list1, list2):
    
    # This is the optimized method
    result = ListNode()
    curr = result
    
    # Run in the loop to compare the two current value of two lists
    while list1 and list2:
        # Whichever node has smaller value, add it to the result list
        if list1.val <= list2.val:
            curr.next = ListNode(list1.val)
            list1 = list1.next
        else:
            curr.next = ListNode(list2.val)
            list2 = list2.next
        curr = curr.next
    # Check if there's any more nodes from either list
    if list1:
        curr.next = list1
    else:
        curr.next = list2
    
    return result.next
    
    
        
    