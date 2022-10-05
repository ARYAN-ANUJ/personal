# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        lenght=0
        while cur is not None:
            cur=cur.next
            lenght+=1
        head=self.reverse(head,k,lenght)
        return head
        
    def reverse(self,head,k,l):
        prev=None
        temp=cur=fwd=head        
        if k<=l:
            for j in range(k):
                fwd=fwd.next
                cur.next=prev
                prev=cur
                cur=fwd
            head=prev
            temp.next=self.reverse(cur,k,l-k)
        return head
    