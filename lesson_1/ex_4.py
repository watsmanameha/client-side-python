# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
# строкового представления в байтовое и выполнить обратное преобразование (используя
# методы encode и decode).

s_words = ['разработка', 'администрирование', 'protocol', 'standard']
b_words = []

for word in s_words:
    b_words.append(word.encode('utf-8'))

print(b_words)

i = 0
for word in b_words:
    b_words[i] = word.decode('utf-8')
    i += 1

print(b_words)

