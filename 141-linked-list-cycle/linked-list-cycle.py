# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:  

        # Hair and Tortoise Algorithm - 2 pointer Algo (slo and fast) it will always detect a cycle 

        slow, fast = head, head 

        while fast and fast.next : 
            slow = slow.next 
            fast = fast.next.next 

            if slow == fast : 
                return True 

        return False 


        '''
        Visualise - 1-> 2 -> 3 -> 4 -> 5 -> 2 

                    s   s    s    s    s 
                        s
                    f        f         f  
                        f         f  
                        f 

        ''' 
        

        