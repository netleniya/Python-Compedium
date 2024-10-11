class Header:
    def __init__(self, text: str):
        self.text = text

    def get_representation(self):
        return self.text.upper()


class LiteralText:
    def __init__(self, text: str):
        self.text = text

    def get_representation(self):
        return self.text


class HorizontalLine:
    def __init__(self, width: int):
        self.width = width

    def get_representation(self):
        return "-" * self.width


def show_document(doc):
    for element in doc:
        print(element.get_representation())


def main() -> None:

    document: list = [
        Header("the open-closed principle"),
        HorizontalLine(25),
        LiteralText(
            "The open-closed principle states that classes should be open for extension, but closed for modification."
        ),
    ]
    show_document(document)


if __name__ == "__main__":
    main()
