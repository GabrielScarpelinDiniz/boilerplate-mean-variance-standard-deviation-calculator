import numpy as np

def calculate(list):
    print(len(list))
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.") 
    calculations = {}

    np_array = np.array(list)
    matrix = np_array.reshape(3, 3)


    column_mean = np.mean(matrix, axis=0)
    row_mean = np.mean(matrix, axis=1)
    elements_mean = np.mean(matrix)
    calculations['mean'] = [column_mean.tolist(), row_mean.tolist(), elements_mean]

    column_variance = np.var(matrix, axis=0)
    row_variance = np.var(matrix, axis=1)
    elements_variance = np.var(matrix)
    calculations['variance'] = [column_variance.tolist(), row_variance.tolist(), elements_variance]

    column_std = np.std(matrix, axis=0)
    row_std = np.std(matrix, axis=1)
    elements_std = np.std(matrix)
    calculations['standard deviation'] = [column_std.tolist(), row_std.tolist(), elements_std]
    
    column_max = np.max(matrix, axis=0)
    row_max = np.max(matrix, axis=1)
    elements_max = np.max(matrix)
    calculations['max'] = [column_max.tolist(), row_max.tolist(), elements_max]

    column_min = np.min(matrix, axis=0)
    row_min = np.min(matrix, axis=1)
    elements_min = np.min(matrix)
    calculations['min'] = [column_min.tolist(), row_min.tolist(), elements_min]

    column_sum = np.sum(matrix, axis=0)
    row_sum = np.sum(matrix, axis=1)
    elements_sum = np.sum(matrix)
    calculations['sum'] = [column_sum.tolist(), row_sum.tolist(), elements_sum]

    return calculations