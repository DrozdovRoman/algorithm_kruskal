import os
from pathlib import Path


def read_matrix(path, sizeof):
    result = []
    with open(path, "r") as textFile:
        for element in textFile:
            element = element.split()
            if len(element) > sizeof:
                element = [int(i) if i.isdigit()
                           else 0 for i in element[0:sizeof]]
                result.append(element)
                continue
            element = [int(element[i])
                       if i < len(element) and element[i].isdigit()
                       else 0 for i in range(sizeof)]
            result.append(element)
        if len(result) < sizeof:
            result.extend([[0 for j in range(sizeof)]
                           for i in range(sizeof - len(result))])
    return (result)


def file_exist(path, format):
    if os.path.exists(path) and Path(path).suffix == format:
        return True
    else:
        return False
