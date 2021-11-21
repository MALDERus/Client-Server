# Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

def type_content_check(words_list):
    for word in words_list:
        print(f'Слово "{word}" с типом {type(word)}')


words_list_str = ['разработка', 'сокет', 'декоратор']

type_content_check(words_list_str)

words_list_utf = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                  '\u0441\u043e\u043a\u0435\u0442',
                  '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

type_content_check(words_list_utf)