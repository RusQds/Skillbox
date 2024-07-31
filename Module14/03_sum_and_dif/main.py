# TODO в Python принято давать имена в стиле
#	 lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
#    По этой причине PyCharm и подсвечивает имена ваших функций и переменных
def sumNumbers(number):
    sumNumber = 0
    while number != 0:
        reNumber = number % 10
        sumNumber += reNumber
        number = number // 10
    return sumNumber


def countNumbers(number):
    count = 0
    while number != 0:
        count += 1
        number = number // 10
    return count


def difference(number):
    differenceNumbers = sumNumbers(number) - countNumbers(number)
    return differenceNumbers


number = int(input('Введите число: '))

print('Сумма цифр:', sumNumbers(number))
print('Кол-во цифр в числе', countNumbers(number))
print('Разность суммы и кол-ва цифр:', difference(number))

# Принято
