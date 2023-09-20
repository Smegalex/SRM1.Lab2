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
    print(f"Масив рандомних цілих чисел від 1 до N без повторів:\n{arr}")

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





def chooseTask(N):
    match N:
        case 1:
            print("Завдання 1.")
            arrayOneToNineNineNine()
        case 2:
            print("Завдання 2.")
            unlimitedNumbersArrification(14, 13, -6, 0, 8, -18)
        case 3:
            print("Завдання 3.")
            choice = input("Оберіть варіант завдання (1-2):")
            if choice == 1:
                arrSmallToLarge([14, 13, -6, 0, 8, -18, 17, 42, -1, 4])
            elif choice == 2:
                arrLargeToSmall([14, 13, -6, 0, 8, -18, 17, 42, -1, 4])
            else:
                print("Немає такого варіанту завдання.")
