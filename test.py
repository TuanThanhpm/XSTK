import numpy as np

np.random.seed(0)

def swap_rows(mat, i , j):
    mat[[i, j]] = mat[[j, i]]
    return mat

def multiply_number(mat, i, num):
    mat[i] = [x* num for x in mat[i]]
    return mat

def add_rows(mat, i, j, num):
    mat[i] = [mat[i][x] + mat[j][x] * num for x in range(len(mat[i]))]
    return mat

def initialize_matrix():
    rows, cols = map(int, input("Input row and column: ").strip().split())
    equations_1 =  '3 -3 3 -1 -5 2 0 -4 2 3 -1 2'# '4 -2 -4 2 6 -3 0 -5 8 -4 28 -44 -8 4 -4 12'
    equations_2 = '2 -3 4 -1 6 1 -8 9 2 6 1 -1'
    result_1 =  '1 3 11 -5'
    result_2 = '-3 4 2 -4'#'0 0 0'
    # single line separated by space
    entries_e = list(map(float, equations_1.split()))
    entries_r = list(map(float, result_2.split()))
    # For printing the matrix
    mat_A = np.array(entries_e).reshape(rows, cols)
    mat_B = np.array(entries_r).reshape(rows, 1)
    
    return mat_A, mat_B, rows, cols

def gauss(mat_A, mat_B, rows, cols):
    pivot_r, pivot_c = 0, 0
    while(pivot_c != cols and pivot_r != rows ):
        arr = [index for index in range(pivot_r, rows) if mat_A[index][pivot_c] != 0]
        arr = np.sort(arr)
        if len(arr) == 0:
            pivot_c = pivot_c + 1
        else:
            mat_A = swap_rows(mat_A, arr[0], pivot_r)
            mat_B = swap_rows(mat_B, arr[0], pivot_r)
            
            if len(arr) != 1:
                pivot_element = mat_A[pivot_r][pivot_c]
                if pivot_element != 1:
                    num = 1 / pivot_element
                    mat_A = multiply_number(mat_A, pivot_r, num)
                    mat_B = multiply_number(mat_B, pivot_r, num)

                for r_index in arr[1:]:
                    num = -(mat_A[r_index][pivot_c] / mat_A[pivot_r][pivot_c])
                    mat_A = add_rows(mat_A, r_index, pivot_r, num)
                    mat_B = add_rows(mat_B, r_index, pivot_r, num)
                # for r_index in range(0, pivot_r):
                #     num = -(mat_A[r_index][pivot_c] / mat_A[pivot_r][pivot_c])
                #     mat_A = add_rows(mat_A, r_index, pivot_r, num)
                #     mat_B = add_rows(mat_B, r_index, pivot_r, num)        
            pivot_r, pivot_c = pivot_r + 1, pivot_c + 1
    return mat_A, mat_B
            
if __name__ == '__main__':
      # seed for reproducibility -> trả về 1 giá trị như nhau
    mat_A, mat_B, rows, cols = initialize_matrix()
    
    print(mat_A)
    print('------------')
    print(mat_B)
    mat_A, mat_B = gauss(mat_A, mat_B, rows, cols)
    print('------------')
    print(mat_A)
    print('------------')
    print(mat_B)
    