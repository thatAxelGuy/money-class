from money import Money


def test_money_creation():
    money = Money(50, "USD")

    assert money.amount == 50
    assert money.currency == "USD"


def test_money_string():
    money = Money(50, "USD")

    assert str(money) == "50.00 USD"


def test_convert_usd_to_eur():
    money = Money(50, "USD")

    result = money.convert_to("EUR")

    assert result.currency == "EUR"
    assert result.amount == 50 * Money.conversion_rates["EUR"]


def test_convert_eur_to_usd():
    money = Money(50, "EUR")

    result = money.convert_to("USD")

    assert result.currency == "USD"
    assert result.amount == 50 / Money.conversion_rates["EUR"]


def test_add_number():
    money = Money(10, "USD")

    result = money + 5

    assert result.amount == 15
    assert result.currency == "USD"


def test_add_money_same_currency():
    first = Money(10, "USD")
    second = Money(5, "USD")

    result = first + second

    assert result.amount == 15
    assert result.currency == "USD"


def test_add_money_different_currency():
    first = Money(10, "USD")
    second = Money(5, "EUR")

    result = first + second

    expected = 10 + (5 / Money.conversion_rates["EUR"])

    assert result.amount == expected
    assert result.currency == "USD"


def test_multiply_money():
    money = Money(10, "USD")

    result = money * 3

    assert result.amount == 30
    assert result.currency == "USD"


def test_operations_return_new_money():
    money = Money(10, "USD")

    result = money + 5

    assert result is not money
    assert money.amount == 10
