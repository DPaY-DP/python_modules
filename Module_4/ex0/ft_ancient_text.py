import sys
import typing


def print_text(file_opened: typing.IO) -> None:
    content = file_opened.read()
    print(content)


def main() -> None:
    total_args = len(sys.argv)-1
    if total_args != 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1], "r")
        print("---")
        print()
        print_text(f)
        print()
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()
