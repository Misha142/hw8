def readall(nm):
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            print(line.strip())

def write_1(nm):
    str_new1 = input('Фамилия: ')
    str_new2 = input('Имя: ')
    str_new3 = input('Отчество: ')
    str_new4 = input('Телефон: ')
    str_new = '\n' + str_new1 + ', ' + str_new2+ ', ' + str_new3+ ', ' + str_new4
    with open(nm, 'a', encoding='utf8') as txt_file:
        txt_file.write(str_new)

def find_item(nm):
    item = input('Характеристика: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            if item.lower() in line.lower():
                print(line.strip())

def find_item_2(nm):
    item = input('Что ищем: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            if item.lower() in line[item_type].lower():
                print(*line)

def sort_data(nm):
    list_1 = []
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        for line in txt_file:
            line = line.split(', ')
            list_1.append(line)
        list_1.sort(key=lambda person: person[item_type])
    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in list_1:
            line = ', '.join(line)
            txt_file.write(line)

def change_data(nm):
    item = input('Что меняем?: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    new_value = input('Введите новое значение: ')
    with open(nm, 'r', encoding='utf8') as txt_file:
        lines = txt_file.readlines()
    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in lines:
            line = line.strip().split(', ')
            if line[item_type].lower() == item.lower():
                line[item_type] = new_value
            txt_file.write(', '.join(line) + '\n')

def delete_data(nm):
    item = input('Что удаляем?: ')
    item_type = int(input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(nm, 'r', encoding='utf8') as txt_file:
        lines = txt_file.readlines()
    with open(nm, 'w', encoding='utf8') as txt_file:
        for line in lines:
            line = line.strip().split(', ')
            if line[item_type].lower() != item.lower():
                txt_file.write(', '.join(line) + '\n')


file_txt='Data.txt'
readall(file_txt)
#write_1(file_txt)
#find_item(file_txt)
#find_item_2(file_txt)
#sort_data(file_txt)
#delete_data(file_txt)
#change_data(file_txt)

readall(file_txt)