# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]: 
        if not root : return [] 

        ans = [] 
        que = deque() 
        que.append(root) 

        while que :  
            row_size = len(que) 
            row_max = float('-inf') 

            for i in range(row_size):
                node = que.popleft() 

                row_max = max(row_max, node.val) 

                if node.left : que.append(node.left) 
                if node.right : que.append(node.right) 

            ans.append(row_max) 

        return ans 


            
            



        