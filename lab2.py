import numpy as np

#1.
def arrayOneToNineNineNine():
    arrayOneToNineNineNine = list(range(1000))
    print(arrayOneToNineNineNine)

#2.
def unlimitedNumbersArrification(*args):
    print (f"Усі аргументи у вигляді масиву:\n{args}")

#3.
def arrSmallToLarge(arr):
    arr = np.sort(arr)
    print(f"Масив за зростанням:\n{arr}")

def arrLargeToSmall(arr):
    arr = np.sort(arr)[::-1]
    print(f"Масив за спаданням:\n{arr}")

#4.
def arrTogether(arr1, arr2):
    arr3 = np.sort((arr1+arr2))
    print(f"Перший масив об'єднаний з другим відсортовані за зростанням:\n{arr3}")

def arrToArr(arr1, arr2):
    arr1 = np.sort((arr1+arr2))
    print(f"Перший масив об'єднаний з другим без використання третього відсортовані за зростанням:\n{arr1}")

#5.
def RandomArray(N):
    arr = []
    for i in range(N):
        while True:
            randomized = np.random.randint(1, N+1, None, int)
            if arr.count(randomized) < 1:
                arr.append(randomized)
                break
    print(f"Масив рандомних цілих чисел від 1 до {N} без повторів:\n{arr}")

#6.
def arrayReshape():
    arr = np.array(np.arange(1.0,101.0,1))
    print (f"Одновимірний масив:\n{arr}")
    b = np.reshape(arr, (10, 10))
    print (f"Матриця 10 на 10:\n{b}")

#7. ?????????
def arrToString():
    arr = np.arange(1, 101).reshape((10, 10))
    arrInString = np.array2string(arr, separator=',', suppress_small=True)
    print (f"Матриця {arr} у формі рядка:\n{arrInString}")

#8.
def vectorLineToColumn():
    vectorLine = np.arange(1, 101).reshape((1, -1))
    vectorColumn = np.reshape(vectorLine, (-1, 1))
    print(f"Вектор-рядок:\n{vectorLine}\nВектор-стовпець:\n{vectorColumn}")

#9.
def oneTwoThreeRepeating():
    oneTwoThreeRepeatingTenTimes = np.resize(np.arange(1,4),(1, 30))
    print(f"1 2 3 три рази:\n{oneTwoThreeRepeatingTenTimes}")

#10.
def zeroArray():
    zeros = np.zeros((10, 10))
    print (f"Нульова матриця 10 на 10:\n{zeros}")

#11.
def smallestAndLargestToVector ():
    arr = np.array([[15, 8, -2], [36, 1, 0], [9, 12, 4], [6, 29, -3]])
    print(f"Дано матрицю:\n{arr}")
    arr = np.split(np.sort(arr, None),2)
    arrSmall = arr[0]
    arrBig = arr[1]
    print(f"Вектор менших чисел:\n{arrSmall}\n\nВектор більших чисел:{arrBig}")

#12. 24 - Обчислити добуток найбільшого й найменшого елемента масива
def multiplyBiggestAndSmallest(arr):
    min = np.amin(arr)
    max = np.amax(arr)
    multiply = min * max
    print(f"Добуток найменшого та найбільшого значення масиву {arr}:\n{multiply}")

#13. 
def onlyOnceWords (arr1, arr2):
    onlyOnce = []
    print(f"Дано масиви:\n{arr1}\n{arr2}")
    for i in arr1:
        if (arr2.count(i) == 0) & (onlyOnce.count(i) == 0) & (arr1.count(i) == 1):
            onlyOnce.append(i)
    for i in arr2:
        if (arr1.count(i) == 0) & (onlyOnce.count(i) == 0) & (arr2.count(i) == 1):
            onlyOnce.append(i)
    print(f"Слова, що були тільки 1 раз:\n{onlyOnce}")

#14.
def monthsSeasons():
    months = np.array(['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'ВЕРЕСЕНЬ', 'Жовтень', 'Листопад', 'Грудень'])
    december = months[-1]
    months = np.delete(months, 1, 0)
    months = np.insert(months, 0, december)
    tuplerisation = np.reshape(months, (-1, 3))
    tuplerisation = tuple(map(tuple, tuplerisation))
    print(f"Було {months}, сформовано в кортежі:\n{tuplerisation}")

def chooseTask(i):
    match i:
        case 1:
            print("Завдання 1.")
            arrayOneToNineNineNine()
        case 2:
            print("Завдання 2.")
            unlimitedNumbersArrification(14, 13, -6, 0, 8, -18)
        case 3:
            print("Завдання 3.")
            choice = int(input("Оберіть варіант завдання (1-2):"))
            if choice == 1:
                arrSmallToLarge([14, 13, -6, 0, 8, -18, 17, 42, -1, 4])
            elif choice == 2:
                arrLargeToSmall([14, 13, -6, 0, 8, -18, 17, 42, -1, 4])
            else:
                print("Немає такого варіанту завдання.")
        case 4:
            print("Завдання 4.")
            choice = int(input("Оберіть варіант завдання (1-2):"))
            if choice == 1:
                arrTogether([14, 13, -6, 0, 8, -18, 17, 42, -1, 4],[12, -37, -2, 94, 25, 5])
            elif choice == 2:
                arrToArr([14, 13, -6, 0, 8, -18, 17, 42, -1, 4],[12, -37, -2, 94, 25, 5])
            else:
                print("Немає такого варіанту завдання.")
        case 5:
            print("Завдання 5.")
            RandomArray(int(input("Введіть натуральне число N:")))
        case 6:
            print("Завдання 6.")
            arrayReshape()
        case 7:
            print("Завдання 7.")
            arrToString()
        case 8:
            print("Завдання 8.")
            vectorLineToColumn()
        case 9:
            print("Завдання 9.")
            oneTwoThreeRepeating()
        case 10:
            print("Завдання 10.")
            zeroArray()
        case 11:
            print("Завдання 11.")
            smallestAndLargestToVector ()
        case 12:
            print("Завдання 12.")
            multiplyBiggestAndSmallest([14, 13, -6, 0, 8, -18, 17, 42, -1, 4])
        case 13:
            print("Завдання 13.")
            onlyOnceWords(['кіт', 'в', 'слон', 'виноград', 'мене', 'кіт', 'моцарела', 'день'],['слон', 'народження', 'моцарела', 'виноград'])
        case 14:
            print("Завдання 14.")
            monthsSeasons()

chooseTask(int(input("Оберіть завдання (1-18):")))