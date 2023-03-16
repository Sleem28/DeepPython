#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
#Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

things = {'axe': 2.0,
          'bowler hat': 1.5,
          'set of plates': 0.75,
          'knife': 0.3,
          'rope': 0.5,
          'tent': 3.5,
          'warm clothes': 2.1,
          'Gum boots': 1.8,
          'set of cups': 1.0,
          'food': 5.2}

weight_limit = 5.0
backpack = dict()
backpack_weight = 0

for key,val in things.items():
    if backpack_weight + val <= weight_limit:
        backpack[key] = val
        backpack_weight += val
    else:
        break

print(backpack)
    



