# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, head)
        prev, curr = d, head # 0, 1

        while curr and curr.next:
            nxt = curr.next.next # 3
            second = curr.next # 2 

            second.next = curr # 1
            curr.next = nxt # 3
            prev.next = second # 2

            prev = curr # 1
            curr = nxt # 3

        return d.next # skipping 0, next is 2

