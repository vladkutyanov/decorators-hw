import sys
from datetime import datetime

# ## Задача 1


def my_write(string_text):
    time_str = '[' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + ']: '
    all_line = time_str + string_text
    original_write(all_line + '\n')


# ## Задача 2


def timed_output(function):
    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        function(*args, **kwargs)
    return wrapper


@timed_output
def print_greeting(name):
    sys.stdout.write(f'Hello, {name}!')


# ## Задача 3


def redirect_output(filepath):
    def decorator(function):
        def wrapper():
            sys.stdout = open(filepath, 'w')
            function()
            sys.stdout.close()
            return 0
        return wrapper
    return decorator


@redirect_output('./function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    original_write = sys.stdout.write
    sys.stdout.write = my_write
    sys.stdout.write('1, 2, 3')
    sys.stdout.write = original_write
    print_greeting("Vlad")
    calculate()
