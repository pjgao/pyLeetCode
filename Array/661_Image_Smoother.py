'''

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

思路：行的-1 0 1和列的-1 0 1排列组合，可用intertools或for i in [-1,0,1] for j in [-1,0,1]
'''
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        import itertools
        r = len(M)
        c = len(M[0])
        #error [[]]*c
        #N = [[None]*c]*r
        N = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                vec = [M[i+x][j+y] for x,y in itertools.product([-1,0,1],[-1,0,1]) if 0 <= i+x < r and 0 <= j+y < c]
                N[i][j] = sum(vec)//len(vec)
        return N