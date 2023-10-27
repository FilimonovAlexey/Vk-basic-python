# Нужно написать программу, которая будет считывать со стандартного ввода целочисленные границы 
# промежутка (сначала левая, потом правая, каждая на отдельной строке). А дальше будет считывать 
# целые числа со стандартного ввода пока не встретит пустую строку, которая будет означать конец ввода. 
# Нужно будет проверить входят ли все введенные числа в промежуток, проверка включает в себя границы промежутка.

left_bound = int(input())
right_bound = int(input())

numbers = []
num = input()

while num != "":
    numbers.append(int(num))
    num = input()
    
# Проверка чисел
all_in_range = True

for number in numbers:
    if number < left_bound or number > right_bound:
        all_in_range = False
        break

if all_in_range:
    print("True")
else:
    print("False")
