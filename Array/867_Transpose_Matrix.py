'''
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
'''
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(*zip(A))
        
    def transpose2(self, A):
    '''
    使用列表推导式，对于对称矩阵，直接交换对焦
    '''
        if len(A) == len(A[0]):
            for i in range(len(A)):
                for j in range(i+1,len(A[0])):
                    A[i][j],A[j][i] = A[j][i],A[i][j]
            return A
        else:
            return [[j[i] for j in A] for i in range(len(A[0]))]
        #return [[j[i] for j in A] for i in range(len(A[0]))]
        