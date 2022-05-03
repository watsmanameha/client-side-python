# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

s_words = ['class', 'function', 'method']

words_in_b = ['\x63\x6c\x61\x73\x73', '\x66\x75\x6e\x63\x74\x69\x6f\x6e', '\x6d\x65\x74\x68\x6f\x64']

for word in words_in_b:
    print(type(word), word, len(word))

