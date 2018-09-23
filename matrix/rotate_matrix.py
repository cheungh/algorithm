def print_matrix(a):
    height = len(a)
    for i in range(0, height):
        width = len(a[i])
        str = ""
        for j in range(0, width):
            str += "%s " % a[i][j]
        print(str)

def rotate_matrix(mat):
    import sys

    left = 0
    top = 0
    bottom = len(mat) - 1
    right = len(mat[0]) - 1

    while top < bottom and right > left:
        # first element to be moved is row [top + 1] column [left]
        prev = mat[top + 1][left]

        # 1. top row go right -> starting from left
        i = left
        while i < right + 1:
            cur = mat[top][i]
            mat[top][i] = prev
            prev = cur
            i += 1
        top += 1

        # right column go DOWN from top
        i = top
        while i < bottom + 1:

            cur = mat[i][right]
            mat[i][right] = prev
            prev = cur
            i += 1
        right -= 1

        # bottom row go left <- from starting from right
        i = right
        while i > left - 1:
            cur = mat[bottom][i]
            mat[bottom][i] = prev
            prev = cur
            i -= 1
        bottom -= 1

        # left column go UP from bottom
        i = bottom
        while i > top - 1:
            cur = mat[i][left]
            mat[i][left] = prev
            prev = cur
            i -= 1
        left += 1
    return mat


if __name__ == '__main__':
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    matrix2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]

    print_matrix(matrix)
    matrix = rotate_matrix(matrix)
    print_matrix(matrix)

    print_matrix(matrix2)
    matrix2 = rotate_matrix(matrix2)
    print_matrix(matrix2)
