# Необходимо написать программу, которая будет считывать три числа и выводить их в определенном формате. 
# Первое число целое, второе с плавающей точкой, третье целое неотрицательное. 
# По примерам необходимо определить требуемый формат данных.

num1 = int(input())
num2 = float(input())
num3 = int(input())

print("{:d}".format(num1))
print("{:.2f}".format(num2))
print("{:d}".format(num3))