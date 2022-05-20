# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess


def ping(url=input('Введите ссылку: ')):
    args = ['ping', url]

    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))

ping()
# Введите ссылку: yandex.ru
# PING yandex.ru (77.88.55.77) 56(84) bytes of data.
#
# 64 bytes from yandex.ru (77.88.55.77): icmp_seq=1 ttl=128 time=30.6 ms
#
# 64 bytes from yandex.ru (77.88.55.77): icmp_seq=2 ttl=128 time=31.3 ms
#
# 64 bytes from yandex.ru (77.88.55.77): icmp_seq=3 ttl=128 time=31.7 ms

# Введите ссылку: youtube.com
# PING youtube.com (108.177.14.91) 56(84) bytes of data.
#
# 64 bytes from lt-in-f91.1e100.net (108.177.14.91): icmp_seq=1 ttl=128 time=49.2 ms
#
# 64 bytes from lt-in-f91.1e100.net (108.177.14.91): icmp_seq=2 ttl=128 time=49.0 ms
#
# 64 bytes from lt-in-f91.1e100.net (108.177.14.91): icmp_seq=3 ttl=128 time=49.2 ms

