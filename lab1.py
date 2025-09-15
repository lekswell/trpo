#  На языке Python, C# или C++ (в консольном режиме) напишите программу обработки последовательности чисел.
# Сначала программа запрашивает число N. Затем создает матрицу D(N, N)  из случайных целых чисел (не превышающих
# по модулю 105). Затем определяет среднее значение среди положительных элементов и формирует массив М
# уменьшением элементов из D на это найденное значение.
# Выходные данные – исходная матрица D и матрица M, полученная после перестановки.
import random
N = int(input())
sum = 0
count = 0
matrix = [[random.randint(-5,5) for i in range(N)] for i in range(N)]
for row in matrix:
  print(row)
for i in range(N):
  for j in range(N):
    if matrix[i][j] > 0:
      count += 1
      sum += matrix[i][j]
mid = sum/count
for i in range(N):
  for j in range(N):
    matrix[i][j] -= mid
for row in matrix:
  print(row)