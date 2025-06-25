# Завдання 1

# Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного контексту, тобто з області, де вона була оголошена.
# Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.
# Послідовність Фібоначе 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

def caching_fibonacci(n: int):
    cache_dict = {}

    def fibonacci(n):
        if n < 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache_dict:
            return n
        else:
            cache_dict[n] = fibonacci(n-1) + fibonacci (n+1)
            return cache_dict[n]
    return fibonacci()

# fib = caching_fibonacci()
# print(fib(10))

print(caching_fibonacci(10))