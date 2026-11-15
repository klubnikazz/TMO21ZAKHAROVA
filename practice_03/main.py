# Задание 1
g = (x + 10 for x in [1, 2, 3])

print(list(g))

# Задание 2
def announce(func):
    def wrapper():
        print("Сейчас вызов")
        return func()
    return wrapper

@announce
def hello():
    print("Привет!")

hello()