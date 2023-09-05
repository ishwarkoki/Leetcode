# class Node:
#     def __init__(self, val, next=None, random=None):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution: 
    def copyRandomList(self, head):
        if not head:
            return None
        
        mp = {}
        curr = head
        prev = None
        newHead = None
        
        while curr:
            temp = Node(curr.val)
            mp[curr] = temp
            
            if newHead is None:
                newHead = temp
                prev = newHead
            else:
                prev.next = temp
                prev = temp
            
            curr = curr.next
        
        curr = head
        newCurr = newHead
        
        while curr:
            if curr.random is None:
                newCurr.random = None
            else:
                newCurr.random = mp[curr.random]
            
            newCurr = newCurr.next
            curr = curr.next
        
        return newHead
