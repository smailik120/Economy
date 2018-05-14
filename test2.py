from tkinter import *
import urllib.request
import urllib.parse

instruments = []
instruments_registration = []
list_tags = []
instruments_lk = []


def post_request_authorization():
    data = urllib.parse.urlencode({'login': a.get(), 'password': b.get()})
    if (urllib.request.urlopen("http://127.0.0.1:5000/", data.encode()).read().decode("utf-8")) == "1":
        create_lk_room()
    if len(list_tags) == 0 and len(instruments_lk) == 0:
        list_tags.append("notification about authorization")
        notification = Label(text="Вы неверно ввели логин или пароль")
        notification.pack()


def create_main_room():
    root.title("Добро пожаловать")
    root.geometry("600x600")
    login = Label(text="Введите Логин:")
    message_login = Entry(textvariable=a)
    password = Label(text="Введите Пароль:")
    message_password = Entry(textvariable=b,show="*")
    authorization_button = Button(text="Авторизация", command=post_request_authorization)
    registration_button = Button(text="Регистрация", command=get_request_registration)
    instruments.append(login)
    instruments.append(message_login)
    instruments.append(password)
    instruments.append(message_password)
    instruments.append(authorization_button)
    instruments.append(registration_button)
    packing(instruments)
    root.mainloop()


def create_registration_room():
    login_registration = Label(text="Введите Логин:")
    message_login_registration = Entry()
    password_registration = Label(text="Введите Пароль:")
    message_password_registration = Entry(show="*")
    registration_button_action = Button(text="Регистрация", command=add_user)
    instruments_registration.append(login_registration)
    instruments_registration.append(message_login_registration)
    instruments_registration.append(password_registration)
    instruments_registration.append(message_password_registration)
    instruments_registration.append(registration_button_action)
    packing(instruments_registration)


def create_lk_room():
    root.destroy()
    new_root = Tk()
    login = Label(text="Вы вошли,да вы гений")
    instruments_lk.append(login)
    packing(instruments_lk)
    new_root.mainloop()
def get_request_registration():
    root.destroy()
    create_registration_room()
    root.mainloop()


def add_user(instruments_registration=instruments_registration):

    data = urllib.parse.urlencode({'login': instruments_registration[1].get(), 'password': instruments_registration[3].get()})
    print(urllib.request.urlopen("http://127.0.0.1:5000/registration", data.encode()).read().decode("utf-8") == "1")


def packing(list_instruments):
    for instrument in list_instruments:
        instrument.pack()


root = Tk()
a = StringVar()
b = StringVar()
create_main_room()



