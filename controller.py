import view
import modules as m


def menu_button():
    return int(input('1 - Add new contact \n2 - Export phone book to xml \n'
                     '3 - Show all contacts \n4 - Find a contact by name \n'
                     '5 - Delete contact \n0 - Exit \n'))


def menu():
    while True:
        choise = menu_button()
        print('')
        if choise == 0:
            break
        elif choise == 1:
            m.init_some_data()
        elif choise == 2:
            view.export_to_xml()
        elif choise == 3:
            view.show()
        elif choise == 4:
            view.find_contact(input('Введите имя: '))
        elif choise == 5:
            m.delete_some_data(input('Введите номер, который хотите удалить: '))
    if choise == 0:
        print('Goodbye!')
