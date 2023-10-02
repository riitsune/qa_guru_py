
def test_greeting():
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    print(output)
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle():
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # TODO сосчитайте периметр
    perimeter = (a+b)*2
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = a*b
    assert area == 200


def test_circle():
    from math import pi
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    # TODO сосчитайте площадь
    area = pi*(r**2)
    assert area == 1661.9025137490005
    print(area)
    # TODO сосчитайте длину окружности
    length = 2*pi*r
    print(length)
    assert length == 144.51326206513048


def test_random_list():
    import random
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """

    # TODO создайте список
    list_1 = random.sample(range(1,100), 10)
    list_1_s = sorted(list_1)
    print(list_1_s)
    assert len(list_1_s) == 10
    assert list_1_s[0] < list_1_s[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    new = set(l)
    new_l = list(new)
    print(new_l)
    assert isinstance(new_l, list)
    assert len(new_l) == 10
    assert new_l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Выведите на экран все значения словаря.
    Подсказка: используй встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
