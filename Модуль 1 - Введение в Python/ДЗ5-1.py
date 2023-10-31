# Необходимо написать программу, которая будет считывать три числа и выводить их в определенном формате. 
# Первое число целое, второе с плавающей точкой, третье целое неотрицательное. 
# По примерам необходимо определить требуемый формат данных.

integer_number = int(input(""))
float_number = float(input(""))
non_negative_integer = int(input(""))

print("{:+010d}".format(integer_number))
print("{:10.2f}".format(float_number).replace(" ", "#"))
print("_".join("{:04b}".format(non_negative_integer)[i:i+4] for i in range(0, 16, 4)))