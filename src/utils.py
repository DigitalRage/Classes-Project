import sys

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def get_int(prompt, min_val=None, max_val=None):
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Invalid input. Enter a number.")
            continue

        value = int(value)

        if min_val is not None and value < min_val:
            print(f"Enter a number ≥ {min_val}.")
            continue

        if max_val is not None and value > max_val:
            print(f"Enter a number ≤ {max_val}.")
            continue

        return value
