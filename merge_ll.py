# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def insertEnd(self, val):
        nd = ListNode(val)

        if self.head == None:
            self.head = nd
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = nd
    
    def printNode(self):  
        if self.head is None:
            print("Sorry, linked list is already empty !!")
        else:
            iterator = self.head
            while iterator is not None:
                print(iterator.val)
                iterator = iterator.next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        if not list1:
            return list2
        if not list2:
            return list1

        tempLL = Solution()
        itr1 = list1
        while itr1 is not None:
            tempLL.insertEnd(itr1.val)
            itr1 = itr1.next

        itr2 = list2
        while itr2 is not None:
            tempLL.insertEnd(itr2.val)
            itr2 = itr2.next

        tempLL.head = self.mergeSort(tempLL.head)
        return tempLL.head

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)

        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def sortedMerge(self, left:ListNode, right:ListNode):
        if not left:
            return right
        if not right:
            return left

        if left.val <= right.val:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)

        return result

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        