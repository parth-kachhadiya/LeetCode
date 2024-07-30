class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head:ListNode):
        if not head:
            return head
        else:
            itr1 = head
            itr2 = itr1.next

            while itr2 is not None:
                if itr1.val == itr2.val:
                    itr1.next = itr2.next
                    itr2 = itr1.next
                else:
                    itr1 = itr2
                    itr2 = itr2.next

            return head

n1 = ListNode(4)
# n2 = ListNode(4,n1)
# n3 = ListNode(2,n2)
# n33 = ListNode(2,n3)
# n4 = ListNode(1,n33)

ptr = Solution().deleteDuplicates(n1)

while ptr:
    print(ptr.val)
    ptr = ptr.next