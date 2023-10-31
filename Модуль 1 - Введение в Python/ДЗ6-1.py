# Необходимо написать программу, которая будет считывать со стандартного ввода строку, далее будет приводить ее к нижнему регистру, 
# а также будет заменять символы “!”, “%”, “#”, “@” на пустую строку. В итоге нужно будет вывести в первой строке число 
# замененных символов, а во второй преобразованную строку.

string = input("")
lowercase_string = string.lower()
modified_string = lowercase_string.replace("!", "").replace("%", "").replace("#", "").replace("@", "")

num_replaced_characters = len(string) - len(modified_string)

print("{}".format(num_replaced_characters))
print("{}".format(modified_string))