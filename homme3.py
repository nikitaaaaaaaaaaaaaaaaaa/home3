# 1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# n = int(input())
# x = int(input())
# list = []
# for i in range (n):
# list.append(i)
# print(list)
# for i in list:
# t = 0
# if i == x:
# t = t + 1
# print (t)

# n = int(input())
# x = int(input())
# list = [i for i in range (1,n)]
# list2 = []
# for i in range (n-1):
# list2.append(x - list[i])
# print(list)
# n = (list2.index(min(list2)))
# print (list[n])