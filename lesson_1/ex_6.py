# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
# программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale

with open('test_file.txt', 'w', encoding='utf-8') as f_n:
    f_n.write('сетевое программирование\n')
    f_n.write('сокет\n')
    f_n.write('декоратор\n')
    print(f'Кодировка файла - {locale.getpreferredencoding()}')
    # Кодировка файла - cp1251

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
# сетевое программирование
# сокет
# декоратор