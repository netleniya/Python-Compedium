class Header:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_representation(self) -> str:
        return self.text.upper()


class LiteralText:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_representation(self) -> str:
        return self.text


class HorizontalLine:
    def __init__(self, width: int) -> None:
        self.width = width

    def get_representation(self) -> str:
        return "-" * self.width


class BulletList:
    def __init__(self, bullets: list[str]) -> None:
        self.bullets = bullets

    def get_representation(self) -> str:
        return "\n".join(f"- {bullet}" for bullet in self.bullets)


def show_document(doc) -> None:
    for element in doc:
        print(element.get_representation())


def main() -> None:

    document: list = [
        Header("the open-closed principle"),
        HorizontalLine(25),
        LiteralText(
            "The open-closed principle states that classes should be open for extension, but closed for modification."
        ),
        BulletList(["Open", "Closed"]),
    ]
    show_document(document)


if __name__ == "__main__":
    main()
