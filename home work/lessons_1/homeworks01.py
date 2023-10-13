# task 01 == Виправте синтаксичні помилки
print("Hello world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4 * apples

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_1 + side_2 + side_3 + side_4
print(perimetery)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
# """
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?

apple_tree = 4
pear_tree = apple_tree + 5
plum_tree = apple_tree - 2
all_trees = apple_tree + pear_tree + plum_tree
print("In the garden, there are 4 apple trees, and there are 5 more pear trees than apple trees.\n"
      "So, the number of pears will be equal to the number of apple trees plus 5.")
print("Number of pear trees = Number of apple trees(4) + 5 =", pear_tree)
print("In the garden, there are 4 apple trees, and there are 2 less plums than apple trees.\n"
      "So, the number of plums will be equal to the number of apple trees minus 2.")
print("Number of plum trees = Number of apple trees(4) + 2 =", plum_tree)
print("Number of all trees = number of apple_tree + pear_tree + plum_tree = ", all_trees)

# task 08
# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?

morning_temperature = +5
afternoon_temperature = morning_temperature - 10
evening_temperature = afternoon_temperature + 4
print("If the temperature in the morning is 5 degrees and the temperature in the afternoon is 10 degrees less\n"
      "Then to calculate the temperature in the afternoon we need to minus 10 from +5.\n"
      "Afternoon temperature = morning_temperature(+5) - 10 =", afternoon_temperature)
print("If the evening temperature rose by 4 degrees\n"
      "Then we need to plus 4 to the afternoon temperature\n"
      "Evening temperature = afternoon temperature(-5) + 4 =", evening_temperature)

# task 09x
# """
# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?
# """
boys = 24
girls = boys / 2
children_today = (boys - 1) + (girls - 2)
print(children_today)
#
# # task 10
# """
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
# """
book_1_costs = 8
book_2_costs = book_1_costs + 2
book_3_costs = (book_1_costs + book_2_costs) / 2
all_costs = book_1_costs + book_2_costs + book_3_costs
print(all_costs)
