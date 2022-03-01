import numpy as np

matrix = np.random.randint(0, 99, size=(5, 4))

def mini(mtrx):
    min_in_col = []
    for col in range(len(mtrx[0])):              
        min_in_col.append(min([mtrx[row][col] for row in range(len(mtrx))]))
    # print(min_in_col)
    return max(min_in_col)

def mini_np(mtrx):
    return max([min(row) for row in mtrx.transpose()])


if __name__== '__main__':
    print(matrix)
    print(mini(matrix))
    print(mini_np(matrix))