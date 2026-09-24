from __future__ import annotations

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

    def __init__(self, amount: float, currency: str) -> None:
        self.currency = currency
        self.amount = float(amount)


    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"

    def convert_to(self, other_currency: str) -> Money:
        """Convert to another currency by using USD as the base currency."""

        current_rate = self.conversion_rates[self.currency]
        target_rate = self.conversion_rates[other_currency]

        usd_amount = self.amount / current_rate
        new_amount = usd_amount * target_rate

        return Money(new_amount, other_currency)


    def __add__(self, other: float | Money) -> Money:
        if isinstance(other, Money):
            converted_currency = other.convert_to(self.currency)
            new_amount = self.amount + converted_currency.amount
            return Money(new_amount, self.currency)
        else:
            return Money(self.amount + other, self.currency)


    def __mul__(self, other):
        return Money(self.amount * other, self.currency)