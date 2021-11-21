# 3. Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе.

def word_to_byte_type_check(words_list):
    for word in words_list:
        try:
            eval(f'b"{word}"')
        except SyntaxError:
            print(f'слово "{word}" невозможно записать в байтовом типе - bytes can only contain ASCII literal characters')

words_list_str = ['attribute', 'класс', 'функция', 'type']

word_to_byte_type_check(words_list_str)