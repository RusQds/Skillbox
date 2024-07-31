def func_fibo(stop, f_n=0, s_n=1, step = 1):
    result = s_n
    if step != stop:
        f_n, s_n = s_n, f_n + s_n
        result = func_fibo(stop, f_n, s_n, step + 1)
    return result


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(func_fibo(num_pos))