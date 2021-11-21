# 4. Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

def endcode_decode(words_list):
    for word in words_list:
        bytes_word = word.encode('utf-8')
        print(f'Слово "{bytes_word}" с типом {type(bytes_word)}')
        str_word = bytes_word.decode('utf-8')
        print(f'Слово "{str_word}" с типом {type(str_word)}')


words_list_str = ['разработка', 'администрирование', 'protocol', 'standard']

endcode_decode(words_list_str)
