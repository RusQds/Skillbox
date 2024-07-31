
def calculating_math_func(data, fact_dict=dict()):
    if data not in fact_dict:
        result = 1
        for index in range(1, data + 1):
            result *= index
        fact_dict[data] = result
    else:
        result = fact_dict[data]
    result /= data ** 3
    result = result ** 10
    return result

data = int(input('Введите число: '))
calculating_math_func(data)

# Принято





