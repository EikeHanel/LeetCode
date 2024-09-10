# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the numbers in the linked list.
        rev_l1 = self.reverse_list(l1)
        rev_l2 = self.reverse_list(l2)

        # Combine the numbers in the linked list to an integer.
        l1_int = self.list_to_int(rev_l1)
        l2_int = self.list_to_int(rev_l2)

        # Addition of the integers.
        ans_int = self.add_num_return_lst(l1_int, l2_int)

        # Converting new integer list to a linked list.
        ans = self.list_to_link(ans_int)

        # Return answer.
        return self.reverse_list(ans)

    def reverse_list(self, lst):
        """
        Takes a linked list and returns the reverse list
        """
        # Initialize three pointers: curr, prev and next
        curr = lst
        prev = None

        # Traverse all the nodes of Linked List
        while curr is not None:

            # Store next
            next_node = curr.next

            # Reverse current node's next pointer
            curr.next = prev

            # Move pointers one position ahead
            prev = curr
            curr = next_node

        # Return the head of reversed linked list
        return prev

    def list_to_int(self, lst):
        """
        Takes a linked list, combines the numbers to a single integer.
        """
        num = []
        while lst is not None:
            num.append(lst.val)
            lst = lst.next
        lst_int = int(''.join(map(str, num)))  
        return lst_int

    def add_num_return_lst(self, num1, num2):
        """
        Addition of two numbers, returns the answer as a list.
        """
        num = num1 + num2
        ans = [int(n) for n in str(num)]
        return ans

    def list_to_link(self, lst):
        """
        Converts a list to a linked list.
        """
        head = ListNode(lst[0])
        current = head
        for item in lst[1:]:
            current.next = ListNode(item)
            current = current.next
        return head

