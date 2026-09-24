class Money:

    def __init__(self, amount: int, currency: str) -> None:
        self.name = currency
        self.amount = amount


    def __str__(self) -> str:
        return f"{self.amount} {self.name}"