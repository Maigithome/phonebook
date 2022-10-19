import UI
import operations


def button_click():
    UI.print_data("\nВы можете выполнить следующие действия со списком: ")
    answer = UI.input_check_choice(
        "1. Вывод всего телефонного справочника.\n2. Добавление нового номера\n3. Поиск информации\n4. Удаление информации\n5. Сохранить спровочник\n6. Выход\n Введите номер действия: ",
        6)
    if answer == 1:
        operations.show_all()
        button_click()
    elif answer == 2:
        operations.add_new()
        button_click()
    elif answer == 3:
        operations.search()
        button_click()
    elif answer == 4:
        operations.remover()
        button_click()
    elif answer == 5:
        operations.export_to()
        button_click()
    elif answer == 6:
        print()