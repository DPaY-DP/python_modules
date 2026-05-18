import sys
import typing


def read_file(file_name: typing.IO) -> str:
    content = file_name.read()
    print("---")
    print()
    print(content)
    print()
    print("---")
    return content


def main() -> None:
    total_args = len(sys.argv)-1
    if total_args != 1:
        print("Usage: ft_ancient_text.py <file>")
        return
    try:
        f = open(sys.argv[1], "r", encoding='UTF-8')
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        old_file = read_file(f)
        print()
        print("Transform data:")
        print("---")
        print()
        new_text = ""
        for char in old_file:
            if char == "\n":
                new_text += "#\n"
            else:
                new_text += char
        print(new_text)
        print()
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")

    try:
        new_name = input("Enter new file name (or empty): ")
        new_file = open(new_name, "w")
        print(f"Saving data to '{new_name}'")
        for char in new_text:
            new_file.write(char)
        print(f"Data saved in file '{new_name}'.")
    except FileNotFoundError:
        print("Not saving data")
        return
    except PermissionError as e:
        print(f"Error opening file '': {e}")


if __name__ == "__main__":
    main()
