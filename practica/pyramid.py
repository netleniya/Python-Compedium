def decode(message_file):
    with open(message_file, "r") as file:
        lines = file.readlines()

    # Parse the lines into a list of (number, word) tuples
    num_word_pairs = []
    for line in lines:
        num, word = int(line.split()[0]), line.split()[1]
        num_word_pairs.append((num, word))

    # Calculate the pyramid positions (1, 3, 6, 10, 15, ...)
    pyramid_positions = []
    n = 1
    while (n * (n + 1)) // 2 <= len(num_word_pairs):
        pyramid_positions.append((n * (n + 1)) // 2)
        n += 1

    # Extract words that are at the pyramid positions
    position_to_word = {num: word for num, word in num_word_pairs}
    decoded_message = " ".join(
        position_to_word[pos] for pos in pyramid_positions if pos in position_to_word
    )

    return decoded_message


def main() -> None:
    print(msg := decode("sample.txt"))


if __name__ == "__main__":
    main()
