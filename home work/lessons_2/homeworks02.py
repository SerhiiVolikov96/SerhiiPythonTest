# task 01 == Розділіть змінну так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті  ???
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n')

# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800

total_area = black_sea_area + azov_sea_area
print(f"The total area of black and azov seas it's a {total_area} km2\n")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_items = 375291
wh1_p_wh2 = 250449
wh2_p_wh3 = 222950

wh3 = total_items - wh1_p_wh2
wh1 = total_items - wh2_p_wh3
wh2 = total_items - wh1 - wh3

print(f"In warehouse 1 stocked {wh1} items\n"
      f"In warehouse 2 stocked {wh2} items\n"
      f"In warehouse 3 stocked {wh3} items\n")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_quantity = 18
payment_amount = 1179
computer_cost = payment_amount * payment_quantity

print (f"To calculate the cost of the computer, we need to multiply the quantity of payments ({payment_quantity}) by the amount of one payment ({payment_amount})\n"
       f"Then we will know the total cost ({computer_cost})\n")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print(f"Для a остача буде {a}\n"
      f"Для b остача буде {b}\n"
      f"Для c остача буде {c}\n"
      f"Для d остача буде {d}\n"
      f"Для e остача буде {e}\n"
      f"Для f остача буде {f}\n")
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large_quantity = 4
pizza_large_price = 274

pizza_medium_quantity = 2
pizza_medium_price = 218

juice_quantity = 4
juice_price = 35

cake_quantity = 1
cake_price = 350

water_quantity = 3
water_price = 21

total_cost = (pizza_large_quantity * pizza_large_price +
              pizza_medium_quantity * pizza_medium_price +
              juice_quantity * juice_price +
              cake_quantity * cake_price +
              water_quantity * water_price)
print("Загальна вартість замовлення для Іринки:", total_cost, "грн\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photos = 232
photo_in_1_page_max = 8
number_of_pages = all_photos // photo_in_1_page_max
if all_photos % photo_in_1_page_max != 0:
    number_of_pages += 1

print(f"Для того щоб підрахувати скількі знадобится сторінок Ігорю треба зробити наступне \n"
      f"Треба взяти кількість всіх фото ({all_photos}) та разділити іх на кількість фото, яка максімально може бути на сторінці ({photo_in_1_page_max})\n"
      f"Ігорю треба бути мати {number_of_pages} сторінок\n")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
kharkiv_to_budapesht = 1600
petrol_consumption_100 = 9
tank_capacity = 48

total_petrol_amount = (kharkiv_to_budapesht / 100) * petrol_consumption_100
refueling_quantity = total_petrol_amount // tank_capacity
if total_petrol_amount % tank_capacity != 0:
    refueling_quantity += 1

print(f"Для того щоб разрохувати загальну кількість палева, яка знадобидтся для подорожі треба,\n"
      f"Відстань від Харькова до Будапешта ({kharkiv_to_budapesht}(км)) разділити на 100 та помножити на расход палива на 100 км ({petrol_consumption_100}(л))\n"
      f"Загальна кілкість літрів бензину для цієї поїздки буде: {total_petrol_amount} літрів\n")

print(f"Для того щоб разрохувати загальну кількість дозаправок, які знадобляться для подорожі треба,\n"
      f"Кількість палева ({total_petrol_amount}(л)) разділити на місткість ьаку ({tank_capacity}(л))\n"
      f"Загальна кілкість зупинок для цієї поїздки буде: {refueling_quantity} раз")
