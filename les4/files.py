def read_file(path):
    with open(path,"r") as file:
        result = file.readlines()
        if not result :
            raise ValueError("Повторите еще раз")

        return result
    with open(path, "r") as file:
        result = file.readlines()
        if not result:
            raise Exception("Файл пустой")

        return result
    with open(path, "r") as file:
        result = file.readlines()
        if not result:
            raise ZeroDivisionError("Нельзя делить на ноль")

        return result
    with open(path, "r") as file:
        result = file.readlines()
        if not result:
            raise SyntaxError("Неправильно написано")

        return result
    with open(path, "r") as file:
        result = file.readlines()
        if not result:
            raise FileNotFoundError("Такой файл не найден")

        return result



file_path = input("Введите путь к файлу")
file_content = read_file(file_path)
read_file(file_path)
for line in file_content:
    print(line.strip("\n"))