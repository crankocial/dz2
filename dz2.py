import random as rand
import copy


def matrix_create():
    out = []
    inside = []
    print('input the size of matrix nxm n=m= ')
    c = input()
    c = int(c)
    for m in range(c):
        for n in range(c):
            inside.append(rand.randint(1, 10))
        out.append(inside)
        inside = []
    return out


def minor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


M = matrix_create()
print(det(M))
print(M)



