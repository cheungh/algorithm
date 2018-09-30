import sys

def print_matrix(a):
    height = len(a)
    for i in range(0, height):
        width = len(a[i])
        str = ""
        for j in range(0, width):
            str += "%s " % a[i][j]
        print(str)

def rotate_matrix(mat):

    # let col be column needed
    row_cnt = len(mat)

    # let row be row needed
    column_cnt = len(mat[0])

    # python create matrix
    a = [0] * column_cnt
    for i in range(column_cnt):
        a[i] = [0] * row_cnt

    # reverse the rows of original
    i = len(mat) - 1
    start = i
    while i > -1:
        # start with last row
        str = ""
        for j in range(0, len(mat[i])):
            str += "%s " % mat[i][j]
            a[j][start-i] = mat[i][j]
        i -= 1
    return a

if __name__ == '__main__':
    # len is column
    #
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,11,12]
        ]
    matrix2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
    ]

    print("===== output 1 =====")
    print_matrix(matrix)
    matrix = rotate_matrix(matrix)
    print("==========")
    print_matrix(matrix)
    print("===== output 2 =====")
    print_matrix(matrix2)
    matrix2 = rotate_matrix(matrix2)
    print("==========")
    print_matrix(matrix2)
