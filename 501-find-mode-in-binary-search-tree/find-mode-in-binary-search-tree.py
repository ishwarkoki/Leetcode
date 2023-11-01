# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]: 
        count = defaultdict(int) 
        ans = []

        def dfs(node): 
            
            if not node : 
                return 

            count[node.val] += 1 
            dfs(node.left) 
            dfs(node.right) 

        dfs(root)

        max_count = max(count.values()) 
        
        for key, value in count.items(): 

            if value == max_count : 
                ans.append(key) 

        return ans

            


        