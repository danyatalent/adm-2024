#Махров Матвей, БПМ-22-1
def generate_permutations_without_repetition(n, permutation=[], used=set()):

    count = 0
    # Базовый случай: если текущая перестановка содержит все числа от 1 до n,
    # то мы достигли конечной перестановки и выводим её
    if len(permutation) == n:
        print(permutation)
        return

    # Рекурсивно генерируем все возможные перестановки, добавляя неиспользованные числа в текущую перестановку
    for i in range(1, n + 1):
        if i not in used:
            used.add(i)
            permutation.append(i)
            generate_permutations_without_repetition(n, permutation, used)
            permutation.pop()
            used.remove(i)


# Входные данные
n = int(input("Введите количество чисел для перестановки без повторений: "))

# Вызов функции для генерации перестановок без повторений
generate_permutations_without_repetition(n)


def generate_permutations_with_repetition(n, permutation=[]):
    # Базовый случай: если текущая перестановка содержит n чисел, то выводим её
    if len(permutation) == n:
        print(permutation)
        return

    # Рекурсивно генерируем все возможные перестановки, добавляя числа от 1 до n в текущую перестановку
    for i in range(1, n + 1):
        permutation.append(i)
        generate_permutations_with_repetition(n, permutation)
        permutation.pop()


# Входные данные
n = int(input("Введите количество чисел для перестановки с повторениями: "))

# Вызов функции для генерации перестановок с повторениями
generate_permutations_with_repetition(n)