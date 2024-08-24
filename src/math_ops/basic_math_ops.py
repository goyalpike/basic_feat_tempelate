"""Define math functions."""


class Adder:
    def __init__(self, num_a: float = 1.0) -> None:
        """Define an adder."""
        self.num_a = num_a

    def __call__(self, num_b: float) -> float:
        """Add a number to a pre-defined adder."""
        return self.num_a + num_b


class Multiplier:
    def __init__(self, num_a=1.0):
        """Define a multiplier."""
        self.num_a = num_a

    def __call__(self, num_b):
        """Multiply a number to a pre-defined adder."""
        return self.num_a * num_b


def main():
    """Define tests."""
    assert Adder(5)(10) == 15
    assert Adder(4)(5) == 9
    assert Multiplier(3)(10) == 30


if __name__ == "__main__":
    main()
