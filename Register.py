
def register():
    with open("C:/Users/HP/Desktop/students.txt", "a") as file:
        while True:
            name = input("Введите ваше имя: ")
            surname = input("Введите вашу фамилию: ")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            if not check_login_exists(login):
                file.write(f"{login}:{password}\n")
                print("Регистрация прошла успешно!")
                break
            else:
                print("Пользователь с таким логином уже существует. Выберите другой логин.")


def check_login_exists(login):
    with open("C:/Users/HP/Desktop/students.txt", "r") as file:
        for line in file:
            existing_login, _ = line.strip().split(":")
            if existing_login == login:
                return True
    return False


def login():
    while True:
        login = input("Введите ваш логин: ")
        password = input("Введите ваш пароль: ")

        if check_credentials(login, password):
            print("Авторизация успешна!")
            break
        else:
            print("Неправильный логин или пароль. Попробуйте еще раз.")


def check_credentials(login, password):
    with open("C:/Users/HP/Desktop/students.txt", "r") as file:
        for line in file:
            saved_login, saved_password = line.strip().split(":")
            if saved_login == login and saved_password == password:
                return True
    return False


while True:
    print("1. Регистрация")
    print("2. Авторизация")
    print("3. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Выход из программы.")
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")
