# Check if a variable is a Function in Python

def do_math(a, b):
    return a + b


print(callable(do_math))  # 👉️ True
print(callable('hello'))  # 👉️ False

if callable(do_math):
    # 👇️ this runs
    print('The variable is a function')
else:
    print('The variable is NOT a function')