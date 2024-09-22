# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        prev = None
        pos = 1
        pos_temp = {}
        while temp:
            pos_temp[pos] = temp.val
            pos += 1
            temp = temp.next

       
            
        temp = head
        for i in range(len(pos_temp)):
            print(f"i: {i}; temp: {temp.val}")
            if len(pos_temp) <= n:
                head = head.next
                break
            elif i+1 == (len(pos_temp) - n) and temp.next:
                temp.next = temp.next.next
                break
            else:    
                temp = temp.next
        return head
        