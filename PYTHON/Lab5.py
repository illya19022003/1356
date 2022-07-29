def new_list(lis, bot, up):  # task 8
    new_list()
    if upper <= bottom:
        return 'Помилка, upper меньше або дорівнює bottom'
    if bottom < min(lis) or bottom > max(lis):
        return 'Помилка, bottom меньше мінімального елемента списку, або більше максимального'
    if upper > max(lis) or upper < min(lis):
        return 'Помилка, upper меньше мінімального елемента списку, або більше максимального'
    bot = min(lis) + bot
    up = max(lis) - up
    for i in lis:
        if i in range(bot, up):
            new_list.append(i)
    return  new_list


check1 = True
while check1:
    try:
        bottom = int(input("Нижня межа вибірки: "))
        upper = int(input("Верхня межа вибірки: "))
        lis = [i for i in range(bottom, upper)]
        print(new_list(lis, bottom, upper))
        check1 = False
    except Exception as e:
        print("Введіть ціле число!", e)
