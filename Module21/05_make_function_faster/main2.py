def calculating_math_func(data,fact_dict=dict()):
    if data in fact_dict:
        return fact_dict[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        fact_dict[data] = result
        result /= data ** 3
        result = result ** 10
        return result


data = int(input('Введите число: '))
result = (calculating_math_func(data))
print(result)