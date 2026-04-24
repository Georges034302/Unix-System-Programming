#!/usr/bin/env python3

def div(a, b):
    return a / b

def safe_division_prevent():
    print("\n--- Prevent exception ---")

    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))

            if b == 0:
                print("b is zero. Try again.")
                continue

            print("Result:", div(a, b))
            break

        except ValueError:
            print("Enter integers only.")

def safe_division_handle():
    print("\n--- Handle exception ---")

    try:
        a = int(input("a = "))
        b = int(input("b = "))
        print("Result:", div(a, b))

    except ValueError:
        print("Enter integers only.")

    except ZeroDivisionError:
        print("Division by zero was handled.")

def main():
    safe_division_prevent()
    safe_division_handle()

if __name__ == "__main__":
    main()
