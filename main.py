import forex_python.converter
from forex_python.converter import CurrencyRates, CurrencyCodes
import datetime

converter = CurrencyRates()
codes = CurrencyCodes()

valueFrom = input("Enter the value you want to convert:  ")
currencyFrom = input("Enter the currency you want to convert:  ").upper()
print(valueFrom+' '+currencyFrom)

base_symbol = codes.get_symbol(currencyFrom.upper())


def check_symbol(symbol, currency):
    while symbol is None:
        print('The entered symbol is invalid')
        currency = input("Enter the currency:  ").upper()
        symbol = codes.get_symbol(currency.upper())
    if symbol is not None:
        return symbol


base_symbol = check_symbol(base_symbol, currencyFrom)
print(valueFrom,base_symbol)

currencyTo = input("Enter the currency you want to get:  ").upper()
print(currencyTo)
to_symbol = codes.get_symbol(currencyTo.upper())

to_symbol = check_symbol(to_symbol, currencyTo)
print(to_symbol)

today = datetime.date.today()
print("Date of today : ", today)

global rate

try:
    rate = converter.get_rate(currencyFrom, currencyTo, today)

    # rate = c.get_rate("USD", "EUR")
    # The exchange rate is a floating-point number
    # that represents the number of Euros that you can get for one US dollar.

    print(rate)
    total = float(rate) * float(valueFrom)
    print(valueFrom, currencyFrom, " is ", total, currencyTo)
except forex_python.converter.RatesNotAvailableError as e:
    print("Exception: ", e)
