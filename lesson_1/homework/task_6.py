# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
# «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale
import chardet

default_encoding = locale.getpreferredencoding()
print(f'Кодировка по умолчанию в системе: {default_encoding}')

words_list_str = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w') as file:
    for el in words_list_str:
        file.write(f'"{el}"\n')

with open('test_file.txt', 'rb') as file:
    for line in file:
        code = chardet.detect(line)
        line = line.decode(code['encoding'])
        line = line.encode('utf-8')
        print(line.decode('utf-8'))
