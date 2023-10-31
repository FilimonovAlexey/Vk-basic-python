# Необходимо написать программу, которая будет считывать со входа данные последовательностей чисел,
# считать и выводить их среднее значение. Напишите сначала функцию, которая будет принимать строку, 
# а в ответ возвращать среднее значение чисел из нее. А далее применяйте эту функцию к каждой считанной 
# входной последовательности. На вход будут подаваться строки, в которых расположены целые числа, 
# разделенные пробелом. Передача пустой строки будет означать конец входных данных.

def calculate_average(sequence):
    numbers = sequence.split()  # разбиваем строку на отдельные числа
    numbers = list(map(int, numbers))  # преобразуем строки в целые числа
    average = sum(numbers) / len(numbers)  # считаем среднее значение
    return average

while True:
    sequence = input()  # считываем строку с числами
    if sequence == '':
        break  # выходим из цикла, если ввод пустой
    average = calculate_average(sequence)  # вызываем нашу функцию
    print(average)  # выводим среднее значение