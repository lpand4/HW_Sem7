# Запись контакта в файл
def export_to_file(file_name='phone_book.txt', data=''):
    with open(file_name, 'a') as f:
        f.write(f'{data[0]}:{data[1]}\n')


3


# Ввод нового контакта
def init_some_data():
    user_data = ['', '']
    user_data[0] = input('Введите имя контакта: ')
    user_data[1] = input('Введите номер телефона контакта: ')
    export_to_file(data=user_data)


# Удаление контакта
def delete_some_data(number):
    with open('phone_book.txt', 'r') as f:
        lines = f.readlines()

    with open('phone_book.txt', 'w') as file:
        for line in lines:
            data = line.split(':')
            if data[1][0:-1] != number:
                file.write(line)
