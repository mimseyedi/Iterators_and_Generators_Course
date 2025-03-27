class Number(int):
    def __reversed__(self) -> int:
        if self > 9:
            snum = str(self)
            srev = snum[::-1]
            irev = Number(srev)
            return irev
        raise ValueError(
            "A single-digit number cannot be reversed."
        )


x = Number(123)
print(reversed(x))