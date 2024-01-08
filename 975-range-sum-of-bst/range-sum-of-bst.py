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

            if not node : 
                return 

            dfs(node.left, arr)
            arr.append(node.val) 
            dfs(node.right, arr) 

        dfs(root, arr) 

        for num in arr: 
            if num >= low and num <= high : 
                ans += num 

        return ans 

                

        