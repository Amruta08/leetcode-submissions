# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        while curr:
            # Skip nodes will same value as current code
            while curr.next and curr.next.val == curr.val:
                curr = curr.next
            
            # No dups found, move prev forward
            if prev.next == curr:
                prev = curr
            else:
                # Dups were found, skip all dup nodee
                prev.next = curr.next
            
            curr = curr.next
        
        return dummy.next
        