import requests as rq


def get_exchange_rate(from_currency):
    url = f"http://www.floatrates.com/daily/{from_currency.lower()}.json"
    request = rq.get(url).json()
    return request


while True:
    print()
    from_currency = input("Enter the currency you want to convert from: ")

    rates = get_exchange_rate(from_currency)

    money = float(input("Enter the amount of money you want to convert: "))

    while True:
        print()
        to_currency = input("Enter the currency you want to convert to: ")

        rate = float(rates[to_currency.lower()]["rate"])
        print("Exchange rate: ", money * rate)

        if input("Do you want to convert to another currency with the same money? (y/n): ") == "y":
            continue
        elif input("Do you wish to convert from another currency? (y/n): ") == "y":
            break
        else:
            print("Thank you for using this currency exchanger!")
            exit()



