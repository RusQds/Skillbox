count_bots = int(input('Кол-во коньков: '))
bots_list = [int(input('Размер 1 пары: ')) for i in range(count_bots)]
count_people = int(input('Кол-во людей: '))
people_list = [int(input('Размер ноги 1 человека: ')) for i in range(count_people)]
bots_list .sort()
print(bots_list)
people_list.sort()
print(people_list)
result = 0
for people in people_list:
    for boot in bots_list:
        if people <= boot:
            bots_list.remove(boot)
            result += 1
            break

print(f'Наибольшее кол-во людей, которые могут взять ролики: {result}')