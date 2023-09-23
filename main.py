#  # task 3
# a = 3
# print(type(a))
# a = 3.5
# print(type(a))
# a = 'qwerty'
# print(type(a))
# a = True
# print(type(a))
# a = '123'
# print(type(a))
#
# # task 4
# a = 5.7
# b = int(a)
# print(b)
#
# a = -5.7
# b = int(a)
# print(b)
#
# a = 3**39 - int(float(3**9))
# print(a)
#
# # task 5
# a = input('Whats your name?')
# print('Hello, ', a)

# # task 6
# x, y = input('Time: hours, minutes ').split()
# print(int(x) * 60 + int(y))

# # task 7
# a = False
# b = True
# c = False
# print((not a or b) and c)

# task 8
# x = int(input('Years: '))
# if x < 1900 or x > 3000:
#     print('Year is not included in the sample.')
# elif (x % 4 == 0 & x % 100 != 0) or (x % 400 == 0):
#     print('Happy Birthday!')
# else:
#     print('Year is ordinary :(')

# # task 9
# print('~~~Task 9~~~')
# a = 1
# while a <= 20:
#     if a % 2 == 0:
#         print(a, end=' ')
#     a += 1

# # task 10
# print('~~~Task 10~~~')
# x = int(input('Enter the number: '))
# summa = 0
# while x != 0:
#     summa += x
#     x = int(input('Enter the number: '))
#
# print('Sum of number:', summa)

# # task 11
# print('~~~Task 11~~~')
# import math
# x = int(input('Enter the X: '))
# y = int(input('Enter the Y: '))
#
# pizza = (x * y) // (math.gcd(x, y))
#
# print('You need ', pizza, ' slices')

# task 12
# print('~~~Task 12~~~')
# a = 0
# for a in range(1, 20+1):
#     if a % 2 == 0:
#         print(a, end=' ')
#     a += 1

# # task 13
# print('~~~Task 13~~~')
# # ввод данных
# a = int(input('Enter the a: '))
# b = int(input('Enter the b: '))
# c = int(input('Enter the c: '))
# d = int(input('Enter the d: '))
# s = ''
# # формируем шапку таблицы
# for i in range (c, d + 1):
#     s += '\t%s' % i
#
# # заполняем строки таблицы
# for i in range(a, b + 1):
#     s += '\n%s' % i # выводим текущее число из умножаемого столбеца
#     for j in range (c, d + 1):
#         s += '\t%s' % (i * j) # выводим результат умножения соответствующих чисел
# print(s)

# print('~~~Task 14~~~')
# n = int(input("Enter the n: "))
# # Создание матрицы
# matrix = [[0] * n for i in range(n)]
# # Определяем направления движения по спирали
# ref = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# ref_idx = 0
#
# # Определяем начальные координаты и значение
# x, y = 0, 0
# num = 10 # начала с 10, чтобы матрица при выводе была красивая
#
# # Заполнение
# for i in range(n * n):
#     matrix[x][y] = num
#     num += 1
#
#     # Определяем следующие координаты
#     dx, dy = ref[ref_idx]
#     next_x, next_y = x + dx, y + dy
#     # Смена направления
#     if not (0 <= next_x < n and 0 <= next_y < n and matrix[next_x][next_y] == 0):
#         ref_idx = (ref_idx + 1) % 4
#         dx, dy = ref[ref_idx]
#         next_x, next_y = x + dx, y + dy
#     # Обновляем координаты
#     x, y = next_x, next_y
# for row in matrix:
#     print(*row)

# # print('~~~Task 15~~~')
# # import threading
# import time
# from tkinter import messagebox
# def job():
#     # threading.Timer(5.0, job).start()
#     if __name__ == '__main__':
#         messagebox.showinfo('UsefulPython', 'Вы слишком долго смотрели в монитор, теперь посмотрите в окно')
# while True:
#     time.sleep(3)
#     job()

# # print('~~~Task 16~~~')
# import time
# import tkinter as tk
# from tkinter.messagebox import showinfo, askyesno
# from tkinter import *
# from tkinter import messagebox
#
# def job():
#     showinfo(title="Информация", message="Вы слишом долго сидите за компьютером!")
# job()
#
# root = tk.Tk()
# def click():
#     result = askyesno(title='Выбор действия', message='Напомнить об этом?')
#     if result:
#         while True:
#             time.sleep(3)
#             job()
#             click()
#     else:
#         root.destroy()
# tk.Button(text="Принять решение", command=click).pack(anchor="center", expand=1)
# root.mainloop()

####что-то тестовое
# root = tk.Tk()
# root.title('Warning')
# root.geometry("250x200")
# messagebox.askyesno('Вы слишком долго сидите за компьютером', 'Напомнить об этом еще?')
# if askyesno() :
#     showinfo('Понял', 'Напомню еще')
#         while True:
#             time.sleep(10)
#             tk()
#     else:
#         root.destroy()
# root.mainloop()






