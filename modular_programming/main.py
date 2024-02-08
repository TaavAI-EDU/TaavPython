from src.add import add
from src.subb import subb

def main():

    add_numbers = add(1, 2, 3, 4)
    sub_numbers = subb(1, 2, 3, 4)

    return (add_numbers, sub_numbers)


print(main())