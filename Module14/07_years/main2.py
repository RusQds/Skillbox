from collections import Counter
def year_good_luck(year_start, year_final):
    year_list = [year for year in range(year_start, year_final + 1) if int(max(Counter([int(num) for num in str(year)]).values())) >= 3]
    return year_list

year_start = int(input('Введите первый год: '))
year_final = int(input('Введите второй год: '))
result = list(map(lambda x: print(x), year_good_luck(year_start, year_final)))
