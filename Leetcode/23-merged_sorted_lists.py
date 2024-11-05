def mergeKLists(lists):
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left = lists[:mid]
    right = lists[mid:]

    l1 = mergeKLists(left)
    r1 = mergeKLists(right)
    return merge_two_list(l1, r1)


def merge_two_list(left, right):
    dummy = node = ListNode()

    while left and right:
        if left.val < right.val:
            node.next = left
            left = left.next
        else:
            node.next = right
            right = right.next
        node = node.next
    node.next = left or right

    return dummy.next


if __name__ == "__main__":
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Helper function to convert a list into a linked list
    def build_linked_list(arr):
        # Create a dummy node to make it easier to handle the head node
        dummy = ListNode(0)
        current = dummy
        # Loop over the array and create ListNode for each element
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next  # Return the actual head (skipping the dummy node)

    # Create the matrix as a list of lists
    matrix = [[1, 4, 5], [1, 3, 4], [2, 6]]

    # Convert each list in the matrix to a linked list
    lists = [build_linked_list(lst) for lst in matrix]

    # Now `linked_lists` will contain the head of each linked list corresponding to each sublist

    mergeKLists(lists)

    while lists:
        print(lists.val)
        lists = lists.next
