from money import Money

usd = Money(50, "USD")

#print(usd)
#print(usd.convert_to("EUR"))

eur = Money(50, "USD").convert_to("EUR")
usd_c =Money(50, "EUR").convert_to("USD")
jpy = Money(50, "GBP").convert_to("JPY")

print(eur)
print(usd_c)
print(jpy)

print(jpy + 50)

result = eur + usd_c
print(result)

print(Money(10, "USD") + 5)
print(Money(10, "USD") + Money(5, "USD"))
print(Money(10, "USD") + Money(5, "EUR"))