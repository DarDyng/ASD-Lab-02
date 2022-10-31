"""IMPORT"""
from io import StringIO
import math
from random import randint


def heap_print(tree, total_width=50):  # Прінт дерева
    """
    :param tree:         Масив дерева
    :param total_width:  Ширина дерева ,за замовчуванням 50 символів
    :return:             Нічого
    """
    fill = " "
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write("\n")
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print(output.getvalue())
    print("-" * total_width)
    return


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def min_heapify(array_inside, k):
    l = left(k)
    r = right(k)
    if l < len(array_inside) and array_inside[l] < array_inside[k]:
        smallest = l
    else:
        smallest = k
    if r < len(array_inside) and array_inside[r] < array_inside[smallest]:
        smallest = r
    if smallest != k:
        array_inside[k], array_inside[smallest] = array_inside[smallest], array_inside[k]
        min_heapify(array_inside, smallest)


def build_min_heap(array_inside):
    n = int((len(array_inside) // 2) - 1)
    for k in range(n, -1, -1):
        min_heapify(array_inside, k)


def max_heapify(array_inside, k):
    l = left(k)
    r = right(k)
    if l <= len(array_inside) - 1 and array_inside[l] > array_inside[k]:
        largest = l
    else:
        largest = k
    if r <= len(array_inside) - 1 and array_inside[r] > array_inside[largest]:
        largest = r
    if largest != k:
        array_inside[k], array_inside[largest] = array_inside[largest], array_inside[k]
        max_heapify(array_inside, largest)


def build_max_heap(array_inside):
    n = len(array_inside) // 2 - 1
    for k in range(n, -1, -1):
        max_heapify(array_inside, k)


def heap_sort(array_inside, i):
    sort = []
    if i == 1:
        copy_a = array_inside.copy()
        for i in range(len(array_inside), 0, -1):
            build_max_heap(copy_a)
            sort.append(copy_a[0])
            copy_a[0] = -100000
        return sort
    else:
        copy_a = array_inside.copy()
        for i in range(len(copy_a), 0, -1):
            build_min_heap(copy_a)
            sort.append(copy_a[0])
            copy_a[0] = 100000
        return sort


def heap_max(array):
    build_max_heap(array)
    return array[0]


def heap_extract_max(array):
    print(f"Число {heap_max(array,)} - максимальне,видаленно зі списку")
    array.pop(0)
    build_max_heap(array)
    heap_print(array)


def heap_increase_key(array_inside, i, key):

    if key < array_inside[i - 1]:  # Міняю значення на інше перебудовую дерево
        print("lol")
        # except "wrong!"
    array_inside[i - 1] = key
    while i > 0 and array_inside[(i // 2) - 1] < array_inside[i - 1]:
        array_inside[i - 1], array_inside[(i // 2) - 1] = array_inside[(i // 2) - 1], array_inside[i - 1]
        i = (i) // 2
        heap_sort(array_inside, min_heapify)


def insert_max(array, new_num_for_add):
    build_max_heap(array)
    array.append(new_num_for_add)
    build_max_heap(array)
    heap_print(array)


def heap_min(array):
    build_min_heap(array)
    return array[0]


def heap_extract_min(array):
    print(f"Число {heap_min(array)} - мінімальне,видаленно зі списку")
    array.pop(0)
    build_min_heap(array)
    heap_print(array)


def replace_key(array_inside, i, key):
    array_inside[i] = key
    heap_print(array_inside)


def insert_min(array, new_num_for_add):
    build_min_heap(array)
    array.append(new_num_for_add)
    build_min_heap(array)
    heap_print(array)


def program_menu():
    while True:
        try:

            x = int(input(
                "Введіть:\n0 - Закінчити роботу програми\n1 - Вивести\n2 - Будувати\n3 - Сортувати\n4 - Видалення і повернення елементу\n5 - Додавання елементу\n6 - Заміна\n"))

            if x == 0:
                break

            elif x == 1:

                heap_print(main_array)

            elif x == 2:

                print("Шо будуємо?")
                y = int(input("0 - max_heap - Кучу де елементи зверху до низу з більшого до меншого\n1 - min_heap - Кучу де елементи зверху до низу з меншого до більшого\n"))

                if y == 0:
                    build_max_heap(main_array)
                elif y == 1:
                    build_min_heap(main_array)

            elif x == 3:

                print("Як сортуємо?")
                y = int(input("0 - за зростанням\n1 - за спаданням\n"))
                print(f"Відсортований масив:{heap_sort(main_array, y)}")

            elif x == 4:

                y = int(input("0 - max\n1 - min\n"))
                if y == 0:
                    heap_extract_max(main_array)
                else:
                    heap_extract_min(main_array)

            elif x == 5:

                y = int(input("0 - max\n1 - min\n"))
                number_for_add = int(input("Введіть число для додавання:"))
                if y == 0:
                    insert_max(main_array, number_for_add)
                else:
                    insert_min(main_array, number_for_add)

            elif x == 6:

                print(f"Масив:{main_array}")
                y = int(input("Введіть число яке в несеться в масив:"))
                number_for_add = int(input("Введіть індекс числа яке зімінеться:"))
                replace_key(main_array, number_for_add, y)

        except ValueError:

            print("Щось пішло не так.\nСкоріше всьго було введено неправильні вхідні дані!\nПопробуйте ще раз!")

            continue


main_array = []

if not main_array:
    try:

        array_length = int(input("Введіть довжину масива:"))

        how_fill_array = int(input("Введіть яким чином хочете заповнити масив:\n0 - Автоматично, з допомогою генератора.\n1 - Вручну, кожен елемент.\n"))

        if how_fill_array == 0:

            print("Введіть границі генератора:")
            left_gen_cordon = int(input("Введіть яке найменше число може бути в масиві:"))
            right_gen_cordon = int(input("Введіть яке найбільше число може бути в масиві:"))

            for i in range(array_length):
                main_array.append(randint(left_gen_cordon, right_gen_cordon))

            program_menu()

        elif how_fill_array == 1:

            for x in range(array_length):
                num = int(input("Введіть число:"))
                main_array.append(num)

            program_menu()

    except ValueError:

        print("Щось пішло не так.\nСкоріше всьго було введено неправильні вхідні дані!")
