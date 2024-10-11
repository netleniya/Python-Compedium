class Header:
    def __init__(self, text: str):
        self.text = text


class LiteralText:
    def __init__(self, text: str):
        self.text = text


def show_document(doc):
    for element in doc:
        if isinstance(element, Header):
            print(element.text.upper())
        elif isinstance(element, LiteralText):
            print(element.text)


def main() -> None:

    document: list = [
        Header("the open-closed principle"),
        LiteralText(
            "The open-closed principle states that classes should be open for extension, but closed for modification."
        ),
    ]
    show_document(document)


if __name__ == "__main__":
    main()
