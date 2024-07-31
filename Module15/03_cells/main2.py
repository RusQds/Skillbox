def cell_effect(i):
    effect = int(input(f'Эффективность {i + 1} клетки: '))
    return effect

cell_count = int(input('Кол-во клеток: '))
cell_list = [str(elem) for elem in map(cell_effect, range(cell_count))]
defect_list = [str(elem) for i, elem in enumerate(cell_list) if int(elem) < i]

print(f'Изначальный список эффективности: {' '.join(cell_list)}')
print(f'Неподходящие значения: {' '.join(defect_list)}')