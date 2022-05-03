import locale

f_n = open('test_file.txt', 'w')

f_n.write('сетевое программирование сокет декоратор')

print(locale.getpreferredencoding())

f_n.close()

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
# UTF-8
# сетевое программирование сокет декоратор