def input_int(message):
    while True:
        try:
            result = int(input(message))
        except ValueError:
            print("Повторите еще раз")
        except Exception:
            print("Файл пустой")
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except SyntaxError:
            print("Неправильно написано")
        except FileNotFoundError:
            print("Такой файл не найден")
        else:
            return result
a = input_int("Введите 1 число")
b = input_int("Введите 2 число")

print(f"{a}+{b}={a+b}")


