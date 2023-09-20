import numpy as np

#1.
def arrayOneToNineNineNine():
    arrayOneToNineNineNine = list(range(0,999))
    print(arrayOneToNineNineNine)

#2.
def unlimitedNumbersArrification(*args):
    arr = []
    for i in args:
        arr.append(i)
    print (f"Усі аргументи у вигляді масиву:\n{arr}")

#3.
def arrSmallToLarge(arr):
    arr = arr.sort()
    print(f"Масив за зростанням:\n{arr}")

def arrLargeToSmall(arr):
    arr = arr.sort(True)
    print(f"Масив за спаданням:\n{arr}")

#4.
def arrTogether(arr1, arr2):
    arr3 = (arr1+arr2).sort()
    print(f"Перший масив об'єднаний з другим відсортовані за зростанням:\n{arr3}")

def arrToArr(arr1, arr2):
    arr1 = (arr1+arr2).sort()
    print(f"Перший масив об'єднаний з другим без використання третього відсортовані за зростанням:\n{arr1}")

#5.
def RandomArray(N):
    arr = []
    for i in range(N):
        while True:
            randomized = np.random.randint(1, N+1, 1, int)
            if arr.count(randomized) < 1:
                arr.append(randomized)
                break
    print(f"Масив рандомних цілих чисел від 1 до N без повторів:\n{arr}")

#6.
def arrayReshape():
    arr = np.arrange(1.0,100.0,1).array()
    print (f"Одновимірний масив:\n{arr}")
    b = np.reshape(arr, (10, 10))
    print (f"Матриця 10 на 10:\n{b}")

#7.
def arrToString():
    arr = np.arange(100).reshape((10, 10))
    arrInString = np.array2string(arr)
    print (f"Матриця {arr} у формі рядка:\n{arrInString}")

#8.
def vectorColumnToLine():
    

