# 34 винни пух и рифма
# def rhymes_param(u):
#     abc = list('а е и о у ы э ю я'.split())
#     rhymes_param = list()
#     for i in u:
#         count = 0
#         for  h in i:
#             if h in abc:
#                 count += 1
#         rhymes_param.append(count)
#     return rhymes_param    
# words = input().split()
# print("парам пам-пам" if len(set(rhymes_param(words))) == 1 else "пам парам")

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).           
def print_operation_table(operation, rows = 6, columns = 6):
     
    for i in range (1, rows + 1):
        for j in range (1, columns + 1):
            print(f"{operation(i,j):4}", end= "")
        print()
       
print_operation_table(lambda x, y: x*y)                   