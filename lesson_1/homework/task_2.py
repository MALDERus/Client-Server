# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

def type_content_length_check(words_list):
    for word in words_list:
        print(f'Слово "{word}" с типом {type(word)} и длиной = {len(word)}')


words_list_bytes = [b'class', b'function', b'method']

type_content_length_check(words_list_bytes)
