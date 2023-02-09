exchange_rates = {
    "USD": 1.0,
    "EUR": 0.86,
    "GBP": 0.76,
    "JPY": 109.94,
    "CAD": 1.31,
    "AUD": 1.39,
    "CHF": 0.91
}
def convert(amount, input_currency, output_currency):
    usd_amount = amount / exchange_rates[input_currency]
    output_amount = usd_amount * exchange_rates[output_currency]
    return output_amount

def main():
    while True:
        amount = float(input("Enter the amount you would like to convert: "))
        input_currency = input("Enter the input currency (USD, EUR, GBP, JPY, CAD, AUD, CHF): ")
        output_currency = input("Enter the output currency (USD, EUR, GBP, JPY, CAD, AUD, CHF): ")
        
        if input_currency not in exchange_rates or output_currency not in exchange_rates:
            print("Error: Invalid currency. Please try again.")
            continue

        result = convert(amount, input_currency, output_currency)
        print(f"{amount} {input_currency} is equal to {result} {output_currency}")

        repeat = input("Do you want to convert another amount (yes/no)?: ")
        if repeat == "no":
            break

if __name__ == "__main__":
    main()
