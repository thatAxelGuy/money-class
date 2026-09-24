from typing import ClassVar


class Money:
    conversion_rates: ClassVar[dict[str, float]] = {
        "USD": 1.0,
        "EUR": 0.87653,
        "GBP": 0.75292,
        "JPY": 157.963,
        "AUD": 1.41448,
        "CAD": 1.4089,
        "CHF": 0.82316
    }

    def __init__(self, amount: int, currency: str) -> None:
        self.name = currency
        self.amount = amount


    def __str__(self) -> str:
        return f"{self.amount} {self.name}"