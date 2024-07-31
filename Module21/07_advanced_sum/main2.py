def sum(*args,my_result=0):
    for i in args:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    my_result = sum(j, my_result)
                else:
                    my_result += j
        else:
            my_result += i
    return my_result



print('Ответ: ', sum([[1, 2, [3]], [1], 3]))
print('Ответ: ', sum(1, 2, 3, 4, 5))