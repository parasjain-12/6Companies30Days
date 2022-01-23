"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def dfs(sub_grid):
            if not sub_grid: return
            is_leaf = all(x == sub_grid[0][0] for x in itertools.chain(*sub_grid)) 
            if is_leaf:
                return Node(sub_grid[0][0] == 1, True, None, None, None, None)
            l, w = len(sub_grid), len(sub_grid[0])
            return Node(
                True,
                False,
                dfs([[sub_grid[i][j] for j in range(w//2)] for i in range(l//2)]),
                dfs([[sub_grid[i][j] for j in range(w//2, w)] for i in range(l//2)]),
                dfs([[sub_grid[i][j] for j in range(w//2)] for i in range(l//2, l)]),
                dfs([[sub_grid[i][j] for j in range(w//2, w)] for i in range(l//2, l)])
            )
        
        return dfs(grid)
        
