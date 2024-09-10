# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr is not None and curr.next is not None:
            # example:[18, 6, 10, 3] 
            # Numbers represent the first loop

            # Take current(18) and next(6) value and send it to the gcd function
            gcd_ans = gcd(curr.val, curr.next.val)

            # Set the greates common divisor(6) as a listnode
            new_node = ListNode(gcd_ans)

            # Take all but the current node and put it after the new listnode[6, 6, 10, 3]
            new_node.next = curr.next

            # Take the new listnode and put it into curr.next -> [18, 6, 6, 10, 3]
            curr.next = new_node

            # Set the curr to after the inserted number -> curr [6, 10, 3]
            curr = curr.next.next
        return head

    def gcd(self, a, b):
        '''
        Takes two integers and returns the greates commin divisor
        '''
        while b != 0:
            c = a % b
            a = b
            b = c
        return a

