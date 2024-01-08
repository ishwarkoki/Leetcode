# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = [ ] 
        ans = 0 

        def dfs(node, arr): 
            nonlocal ans 

            if not node : 
                return 

            dfs(node.left, arr)
            if node.val >= low and node.val <= high : ans += node.val
            dfs(node.right, arr) 

        dfs(root, arr) 

        return ans 

        

                

        