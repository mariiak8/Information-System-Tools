# Задача 1: Палиндром
# Напишите программу, которая получает строку введенную с клавиатуры и,
# если введенная строка палиндром, выводит “Да”, иначе выводит “Нет”.

def task1():
    str_pall = input("Введите строку: ")
    str_pall = str_pall.replace(" ", "")
    for i in range(len(str_pall)):
        if str_pall[i].upper() != str_pall[-(i + 1)].upper():
            print("Нет")
            return
    print("Да")

# Задача 2: Минимумы
# Напишите программу, на вход которой подаётся прямоугольная матрица в
# виде последовательности строк (числа пишем через пробел). Используйте
# метод split() строки. После последней строки матрицы идёт строка,
# содержащая только end.
# После того, как пользователь ввел end, программа должна найти в каждой
# строке матрицы минимальное значение и вывести его на экран.

def task2():
    matrix=[]
    while True:
        str = input()
        if str == 'end':
            break
        else:
            matrix.append(list(map(int, str.split())))
    for i in range(len(matrix)):
        print(min(matrix[i]))

# Задача 3: Персонажи
# Напишите простой вариант программы, которая
# подсчитывает сколько различных слов введено и сколько каждое слово
# встречается.
# Программа должна считывать одну строку со стандартного ввода и выводить
# для каждого уникального слова в этой строке число его повторений (без учета
# регистра) в формате "слово : количество".

def task3():
    name = input().lower().split(' ')
    d = dict()
    for i in name:
        d[i] = name.count(i)
    k = 0
    for i in d.items():
        k += 1
        print(k, "." , i,  end="\n")

# Задача 4: MySQL
# Напишите программу, которая создает и отправляет запрос к БД MySQL, мы
# уже создали в MySQL свою БД – my_db.

def task4():
    import pymysql
    import cryptography
    connect = pymysql.connect(host="127.0.0.1",
                          user="root",
                          password="pass",
                          db="my_db")
    sql = "select first_name, last_name, date_of_birth from user where year(date_of_birth) = %s"
    year = input("Введите год: ")
    cur = connect.cursor()
    cur.execute(sql, year)
    for rec in cur:
        print(rec[0], rec[1], rec[2])


print("Task 1")
task1()
print("\nTask 2")
task2()
print("\nTask 3")
task3()
print("\nTask 4")
task4()
