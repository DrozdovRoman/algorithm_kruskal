def FindMinimumSpanningForest(matrix):
    arr = []
    result = []
    relation = [i for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            if matrix[i][j] != 0:
                arr.append([[i, j], matrix[i][j]])
    arr.sort(key=lambda item: item[1])
    for element in arr:
        if relation[arr[0][0][0]] != relation[arr[0][0][1]]:
            relation[arr[0][0][1]] = relation[arr[0][0][0]]
            result.append(arr.pop(0))
        else:
            if len(result) == len(matrix) - 2:
                result.append(arr.pop(0))
                break
            del arr[0]
    print("Минимальное остовное дерево")
    for element in result:
        print(element[0][0] + 1, "-", element[0][1] + 1, " : ", element[1])
