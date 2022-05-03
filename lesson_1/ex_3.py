# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

s_words = ['attribute', 'класс', 'функция', 'type']

for word in s_words:
    print(word.encode('utf-8'))
    # b'attribute' [x]
    # b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'
    # b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
    # b'type' [x]
