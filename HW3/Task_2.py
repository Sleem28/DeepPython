#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
#Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

some_text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. '\
            'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '\
            'when an unknown printer took a galley of type and scrambled it to make a type specimen book. '\
            'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. '\
            'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing '\
            'software like Aldus PageMaker including versions of Lorem Ipsum.'

out_dict = dict()
res_dict = dict()
counter = 10
split_txt = some_text.split()


for item in split_txt:
    item = item.lower()
    last_symbol =  item[len(item)-1]
    if not last_symbol.isalpha():
        item = item.removesuffix('.')
        item = item.removesuffix(',')
    out_dict.setdefault(item, 0)
    out_dict[item] += 1

max_key = max(out_dict.values())

while counter > 0:
    for key, val in out_dict.items():
        if val == max_key:
            res_dict[key] = val
            counter -= 1
            if counter <= 0:
                break
    max_key -= 1
    if max_key == 0:
        break



print(f'Ten maximum frequent words in the text look like: {res_dict}')