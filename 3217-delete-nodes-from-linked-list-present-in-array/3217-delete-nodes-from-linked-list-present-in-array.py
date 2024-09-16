# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        while head and head.val in nums_set:
            head = head.next

        current = head
        while current and current.next:
            if current.next.val in nums_set:
                # Skip the node
                current.next = current.next.next
            else:
                # Only move to the next node if the current node wasn't deleted
                current = current.next
        
        return head