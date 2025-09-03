from myfunc import add_numbers
def main():
    a = int(input("กรอกตัวเลข A: "))
    b = int(input("กรอกตัวเลข B: "))

    result = add_numbers(a, b)

    print(f"ผลลัพธ์ของ {a} + {b} = {result}")

if __name__ == "__main__":
    main()