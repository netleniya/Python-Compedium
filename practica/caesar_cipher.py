import string


def cipher(text: str, shift: int, direction: str) -> None:
    alphabet: list[str] = [*string.ascii_lowercase]

    result: str = ""
    if direction.startswith("dec"):
        shift *= -1

    alphabet.extend(alphabet)

    for char in text:
        if char in alphabet:
            pos: int = alphabet.index(char)
            new_pos: int = pos + shift
            result += alphabet[new_pos]
        else:
            result += char

    print(f"{direction}d text: {result}")


def main() -> None:

    play_on: bool = True
    while play_on:
        answer: str = input("Do you want to play? (y/n): ").lower()
        if answer.startswith("y"):
            direction: str = input(
                "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
            )
            text: str = input("Type your message:\n").lower()
            shift: int = int(input("Type the shift number:\n"))

            shift %= 26
            cipher(text, shift, direction)
        else:
            print("Vale!")
            play_on = False


if __name__ == "__main__":
    main()
