string = "Hello, worcld!"
text=""
for i, char in enumerate(string):
    if i == 2:
        continue
    if char == 'c':
        text ="Найден символ 'c'"
    print(char, end="")
print("\nДлина строки:", len(string))
print("Строка без последнего символа:", string[:-1])
print (text)