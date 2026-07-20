def multiple(a: int, b: int) -> int:
    return a * b

def sub(a: int, b: int) -> int:
    return a - b

def sum(a: int, b: int) -> int:
    return a + b

def input_number_from_console_and_return_it() -> int:
    number = input("Write number: ")

    if type(number) != int:
        raise ValueError("Incorrect input type")

    return number

def main() -> None:
    number = input_number_from_console_and_return_it()
    print(number)

    return 0

if __name__ == "__main__":
    main()
