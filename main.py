from init_matrix import file_exist, read_matrix
if __name__ == "__main__":
    path = "matrix.txt"
    format = ".txt"
    matrixSize = 9
    if file_exist(path=path, format=format):
        matrix = read_matrix(path, sizeof=matrixSize)
    else:
        print("File not found.")
