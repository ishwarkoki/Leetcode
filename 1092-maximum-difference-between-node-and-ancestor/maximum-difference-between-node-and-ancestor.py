# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:


        def dfs(node, mini, maxi): 

            if not node: 
                return abs(mini-maxi)

            mini = min(node.val, mini) 
            maxi = max(node.val, maxi) 

            l = dfs(node.left, mini, maxi) 
            r = dfs(node.right, mini, maxi) 

            return max(l,r)  

        return dfs(root, root.val, root.val)  


            


























        # def bfs(node): 
        #     que = deque() 
        #     que.append(node) 
        #     level = 0  

        #     while len(que) : 
        #         level += 1 

        #         for _ in range(len(que)): 
        #             cur_node = que.popleft() 
        #             if cur_node.left : 
        #                 que.append(cur_node.left) 

                        


        