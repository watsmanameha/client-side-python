# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s_words = ['attribute', 'класс', 'функция', 'type']

for word in s_words:
    try:
        print(bytes(word, 'ascii'))
    except UnicodeEncodeError:
        print(f'"{word}" невозможно записать в байтовом типе')