
menu_list = []
while True:
    try:
        food = input()
        menu_list.append(food)
    except:
        break

f=tuple(menu_list)
print(f)
max(f)




