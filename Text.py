menu = ['Главное меню:',
        '\t1. Открыть файл',
        '\t2. Сохранить файл',
        '\t3. Посмотреть все заметки',
        '\t4. Добавить заметку',
        '\t5. Выбор по дате',
        '\t6. Найти заметку по имени',
        '\t7. Изменить заметку',
        '\t8. Удалить заметку',
        '\t9. Выход\n']

no_phone_book = 'Журнал заметок пуст или не открыт'

input_choice = 'Выберите пункт меню: '

def wrong_choice(limit: int) -> str:
    return f'Вы ввели неверное число. Надо от 1 до {limit}'

open_successful = 'Журнал заметок успешно открыт'
add_successful = 'Заметка успешно добавлена'
save_successаul = 'Журнал заметок успешно сохранен'
load_error = 'Журнал заметок пуст или не открыт'

new_note = ['Введите название заметки: ', 'Введите тело заметки: ']
change_note = ['Введите имя или Enter, что бы оставить без изменений: ',
                'Введите тело заметки или Enter, что бы оставить без изменений: ']
change_choice = 'Выберите заметку для изменения: '

def changed(name:str)-> str:
    return f'Заметка была изменена!'

index_del_contact = 'Введите индекс заметки, который хотите удалить или введите 0 для возврата в главное меню: '

def del_contact(name: str):
    return f'Заметка {name} успешно удалена!'

for_find_data = 'Введите дату для его нахождения(пример 09/12/23 22:34 PM ): '
for_find_name = 'Введите имя заметки для нахождения: '
close = 'Вы вышли из журнала заметок.'