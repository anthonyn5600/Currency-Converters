from currency_data import *

for currency_available in currency:
    print(currency_available)

USD = "United States Dollar"
print(USD, '\n')
while True:
    print("What currency you converting from?: ", end='')

    currency_origin = input()
    if currency_origin in currency or currency_origin == USD:
        print('How much you going to convert?: ', end='')
        dollars = float(input())
        break;
    else:
        print("Invalid currency. ")


print('To what currency?: ', end='')
currency_wanted = input()

if currency_origin == USD and currency_wanted != currency_origin:
    print(dollars * currency[currency_wanted])
elif currency_origin != USD and currency_wanted == USD:
    print(dollars * currency_usdrates[currency_origin])
elif currency_origin != USD and currency_wanted != currency_origin:
    to_usd = dollars * currency_usdrates[currency_origin]
    print(to_usd * currency[currency_wanted])
else:
    print(dollars)

