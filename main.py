from forex_python.converter import CurrencyRates,CurrencyCodes

valueFrom = input("Enter the value you want to convert:  ")
currencyFrom = input("Enter the currency you want to convert:  ")
print(valueFrom+' '+currencyFrom)

converter = CurrencyRates()
codes = CurrencyCodes()

base_symbol = codes.get_symbol(currencyFrom.upper())

if base_symbol is None:
    print('The entered symbol is invalid')
else:
    print(valueFrom+' '+base_symbol)



