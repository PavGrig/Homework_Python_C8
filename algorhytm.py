from func import create
from interface import interface
path = "phone_book.txt"
create(path)
enter = 0
while enter != 6:
    enter = interface()
    if enter == 1:
        from func import add_contact
        stroka = str(input("Введите ФИО и номер телефона через пробел: "))
        add_contact(path, stroka)
    elif enter == 2:
        from func import show_all
        print(show_all(path))
    elif enter == 3:
        from func import search
        stroka = str(input("Введите фамилию: "))
        search(path, stroka)
    elif enter == 4:
        from func import delete
        stroka = str(input("Введите фамилию: "))
        delete(path, stroka)
    elif enter == 5:
        from func import change
        stroka = str(input("Введите фамилию: "))
        change(path, stroka)        
print("Спасибо за работу!!!")