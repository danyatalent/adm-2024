# БПМ-22-1
# Выполнил: Каневский Даниил

# Размещения с повторениями
# наборы длины k в системе счисления n
def arrangements_with_repetitions(n, k):
    # цифры генерируемого числа 
    b = [0 for _ in range(n)]

    # длина размещения = 0
    if k == 0:
        # пустое множество
        return {()}
    
    while b[k] != 1:
        # Вывод текущего размещения в обратном порядке
        for j in range(k-1, -1, -1):
            print(b[j], end="")
        print(" ", end="")
        
        i = 0
        while b[i] == n-1:
            b[i] = 0
            i += 1
        b[i] = b[i] + 1
    print()

def main():
    print("\nГенерация размещений с повторениями.")
    n = int(input("Введите основание системы счисления n: "))
    k = int(input("Введите длину размещений k: "))
    print("Размещения с повторениями:\n")
    arrangements_with_repetitions(n, k)

if __name__ == "__main__":
    main()