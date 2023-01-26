# Показывает весь справочник
def show(file_name='phone_book.txt'):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split(':')
            print(f'Name: {data[0]}, Number: {data[1]}')


# Экспортирует в xml
def export_to_xml(first_file_name='phone_book.txt', second_file_name='phone_book.xml'):
    with open(first_file_name, 'r') as f:
        data = f.readlines()
        with open(second_file_name, 'w') as file:
            for line in data:
                file.write(f'{line}')


# Поиск контакта по имени
def find_contact(name=''):
    with open('phone_book.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name_line = line.split(':')
            if name_line[0] == name:
                print(f'Number - {name_line[1]}')
