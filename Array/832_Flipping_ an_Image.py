'''
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
先逆序，再取反
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
'''
class Solution:
    def flipAndInvertImage(self, A):
        
        #return [[1^j for j in i[::-1]] for i in A]
        #return [[0 if j else 1 for j in i[::-1] ] for i in A]
        #for i in range(len(A)):
        #    A[i].reverse()
        #    for j in range(len(A[i])):
        #        A[i][j] = 1 - A[i][j]
        #return A
        for i in A:
            i.reverse()
            for j in range(len(i)):
                i[j] = 1-i[j]
        return A
         
        