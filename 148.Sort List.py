# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nodes = []
        while head:
            tmp = head.next
            head.next = None
            nodes.append(head)
            head = tmp
        nodes = sorted(nodes, key=lambda x:x.val)
        if len(nodes)<=1:
            return head
        head=nodes[0]
        dummy = head
       # dummy.next=nodes[1]
        for node in nodes[1:]:
            dummy.next = node
            dummy = dummy.next
        return head