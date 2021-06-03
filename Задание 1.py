my_string = "Добро пожалоовать"
start = -1
count = 0

s = "o"

while True:
    start = my_string.find("о", start+1)
    if start == -1:
        break
    count += 1

    if count == 4:
       print("Количество вхождений символа в строку:  \no\no\no\no", )